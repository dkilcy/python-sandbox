'''
Created on Oct 10, 2014

s3performance is a simple tool to measure the performance of PUT, GET and 
DELETE operations within S3.

Uses timeit which is cross-platform and turns off garbage collection by 
default.

Requires FileChunkIO:
# pip install FileChunkIO

References:
http://www.pythoncentral.io/time-a-python-function/
https://docs.python.org/2/library/timeit.html#timeit.Timer.timeit

Tested with:
Python 2.6.6
CentOS release 6.5 (Final)

There is no copyright on this code, so if you can make money with it, good
for you.

@author: dkilcy
'''

import hashlib
import math
import os
import sys
import timeit
import uuid

from optparse import OptionParser

from boto.exception import S3CreateError
#from boto.s3.connection import Location
from boto.s3.connection import S3Connection
from boto.s3.key import Key

from filechunkio import FileChunkIO

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def md5_for_file(path, block_size=4096, hr=False):
    '''
    Block size directly depends on the block size of your filesystem
    to avoid performances issues
    blocksize is 4096 bytes
    max
    blocksize retrieved using:
    [root@workstation-01 ~]$ hdparm -I /dev/sda | grep -i physical
    Physical Sector size:                  4096 bytes

    '''
    md5 = hashlib.md5()
    with open(path,'rb') as f: 
        for chunk in iter(lambda: f.read(block_size), b''): 
            md5.update(chunk)
    return md5

# throughput in MBps, request_size in KB
def calc_IOPS_Mbps(throughput, request_size):
    iops = ( float(throughput)/ float(request_size)) * 1024
    throughput = (iops * float(request_size)) / 1024
    
    return iops, throughput

'''
S3Performance
'''
class S3Performance(object):

    def __init__(self, options):
        
        d = vars(options)
        
        self.bucket = d.get('bucket')
        self.op = d.get('operation')
        self.numfiles = d.get('numfiles')
        self.size = d.get('size') * 1024
        self.access_key = d.get('access_key')
        self.secret_key = d.get('secret_key')
        self.host = d.get('host')
        self.chunk_size = d.get('chunk_size')
        
        self.clean_on_exit = d.get('clean_on_exit')

    def _create_file(self):
                
        filename = uuid.uuid4().get_hex()
        print 'creating file - filename=%s' % filename
        
        # generate a binary file with random data
        with open(filename, 'wb') as fout:
            fout.write(os.urandom(self.size)) 
    
        filesize = os.stat(filename).st_size
        
        md5_checksum = md5_for_file(filename)
            
        print 'created file - filename=%s filesize=%d md5=%s' % (filename, \
            filesize, md5_checksum.hexdigest() )
        
        return filename, filesize, md5_checksum
    
    def _get_S3(self, bucket, filename):       
        
        key = Key(bucket)
        key.key = filename
        key.get_contents_to_filename(filename) 

    def _put_S3(self, bucket, filename, filesize, md5_checksum, chunk_count):
        
        if chunk_count == 0:            
            key = Key(bucket)
            key.key = filename            
            key.set_contents_from_filename(filename) 
            #, md5=md5_checksum.hexdigest() )  
        else:
            mp = bucket.initiate_multipart_upload(os.path.basename(filename))
            
            for i in range(chunk_count + 1):
                offset = self.chunk_size * i
                bytes = min(self.chunk_size, filesize - offset)
                with FileChunkIO(filename, 'r', offset=offset, bytes=bytes) \
                  as fp:
                    mp.upload_part_from_file(fp, part_num=i + 1)
    
            mp.complete_upload()          
        
    def _delete_S3(self, bucket, filename):
        
        key = Key(bucket)
        key.key = filename
        key.delete()
        
    # ====================================================================== #
        
    def run(self):
       
        print 'clean on exit is %s' % self.clean_on_exit
       
        conn = S3Connection(self.access_key, self.secret_key,
            host=self.host)
        
        #print '\n'.join(i for i in dir(Location) if i[0].isupper())
        
        bucket = None
        
        try:
            # try to create bucket if it does not exist
            bucket = conn.create_bucket(self.bucket)
            print 'created bucket %s' % self.bucket            
        except S3CreateError:
            # bucket exists, use it
            bucket = conn.get_bucket(self.bucket)
            print 'got bucket %s' % self.bucket
        
        print bucket
            
        filename, filesize, md5_checksum = self._create_file()

        chunk_count = int(math.ceil(filesize/self.chunk_size))
        
        if chunk_count > 0:
            print 'will use multpart upload'
        else:
            print 'will use regular upload'
            self.chunk_size = filesize
            
        print 'performing operation..(filesize=%d chunk_size=%d ' \
            'chunk_count=%d)' % \
            (filesize, self.chunk_size, chunk_count)
            
        wrapped = None
        
        if self.op == 'GET':
            self._put_S3(bucket, filename, filesize, md5_checksum, 
                         chunk_count)                                                            
            wrapped = wrapper(self._get_S3, bucket, filename)
        elif self.op == 'PUT':
            wrapped = wrapper(self._put_S3, bucket, filename, filesize, \
                              md5_checksum, chunk_count)
        elif self.op == 'DELETE':                 
            wrapped = wrapper(self._delete_S3, bucket, filename)  
        else:
            print "Unknown operation '%s', exiting" % self.op
            sys.exit(-1)
            
        total_time = 0
        min_time = sys.maxint
        max_time = -sys.maxint
           
        total_iops = 0     
        min_iops = sys.maxint
        max_iops = -sys.maxint
          
        total_speed = 0
        min_speed = sys.maxint 
        max_speed = -sys.maxint
        
        # filesize is in bytes        
        filesize_megabits = ((filesize * 8) / 1024.0) / 1024.0
        filesize_kilobytes = filesize / 1024.0
        chunk_size_bits = (self.chunk_size * 8) / 1024
            
        #sanity check      
        #print '%d bytes is %f megabits' % (filesize, filesize_megabits)   

        for i in range(1, (self.numfiles+1) ):     
            
            if self.op == 'DELETE':
                self._put_S3(bucket, filename, filesize, md5_checksum, \
                             chunk_count)

            time = timeit.timeit(wrapped, number=1) #self.numfiles)
            
            # filesize is in bytes
            # time is in seconds                            
            # speed in Mbps
            
            speed = ( filesize_megabits / time) 
            iops, throughput = calc_IOPS_Mbps(speed, chunk_size_bits)
            # make sure the calculation was done correctly
            # speed and throughput should be equal 
            #print 'check: speed=%f throughput=%f' % (speed, throughput)   
                        
            total_time += time  
            if time < min_time:
                min_time = time
            if time > max_time:
                max_time = time 
                
            total_iops += iops
            if iops < min_iops:
                min_iops = iops
            if iops > max_iops:
                max_iops = iops 
               
            total_speed += speed
            if speed < min_speed:
                min_speed = speed
            if speed > max_speed:
                max_speed = speed 

            print 'i=%d time=%0.2f ms; iops=%0.2f op/s; speed=%0.2f Mb/s' \
                % (i, float(time * 1000), iops, speed) 
 
        avg_time = total_time / self.numfiles
        avg_iops = total_iops / self.numfiles
        avg_speed = total_speed / self.numfiles
        
        print "%d %dKB %s's performed (total time=%f ms):" % ( self.numfiles, \
            filesize_kilobytes, self.op, total_time*1000)        
        print " Avg: %0.2f ms;  %0.2f op/s;  %0.2f Mb/s" % \
            ( avg_time, avg_iops, avg_speed )
        print " Max: %0.2f ms;  %0.2f op/s;  %0.2f Mb/s" % \
            ( max_time, max_iops, max_speed )
        print " Min: %0.2f ms;  %0.2f op/s;  %0.2f Mb/s" % \
            ( min_time, min_iops, min_speed )        
        
        conn.close()
    
        if self.clean_on_exit:
            os.remove(filename)
        
if __name__ == '__main__':
    
    parser = OptionParser(usage="\
    \n\
s3performance is a simple tool to measure the performance of PUT, GET and \n\
DELETE commands to S3. Given the number and size of the files to perform \n\
one of the operations on, it will output the average, minimum and maximum \n\
time of each operation, operations per seconds and their speed in Mb/s.")
    
    parser.add_option("-b", "--bucket", help="Bucket Name")
    parser.add_option("-o", "--operation", 
        help="Values are PUT, GET and DELETE")
    parser.add_option("-n", "--numfiles", type="int",
        help="The number of files to perform operations on")
    parser.add_option("-s", "--size", type="int",
        help="The size of the files in KB")
    parser.add_option("-a", "--access_key", 
        help="Access key")
    parser.add_option("-k", "--secret_key", 
        help="Secret key")
    parser.add_option("-c", "--host", default="demo",
        help="Hostname")
    parser.add_option('-u', '--chunk_size', type="int", 
        default=(5 * 1024 * 1024), 
        help="The chunk size for multipart upload in KB.  Default is 5MB" )
    parser.add_option('-x', '--clean_on_exit', 
        action="store_true", dest="clean_on_exit", default=False,
        help="Remove generated files on program exit")
    
    options, args = parser.parse_args()
    
    print options, args
    
    perf = S3Performance(options)

    perf.run()
