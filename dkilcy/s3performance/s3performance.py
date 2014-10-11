'''
Created on Oct 10, 2014

s3performance is a simple tool to measure the performance of PUT, GET and 
DELETE.

Uses timeit which is cross-platform

References:
http://www.pythoncentral.io/time-a-python-function/
http://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator

There is no copyright on this code, so if you can make money with it, good
for you.

@author: dkilcy
'''

import os
import sys
import timeit
import uuid

from optparse import OptionParser

from boto.exception import S3CreateError
#from boto.s3.connection import Location
from boto.s3.connection import S3Connection
from boto.s3.key import Key

#from filechunkio import FileChunkIO

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

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
        
        self.clean_on_exit = True
        
    def _create_file(self):
                
        filename = uuid.uuid4().get_hex()
        print 'creating file - filename=%s' % filename
        
        with open(filename, 'wb') as fout:
            fout.write(os.urandom(self.size)) 
    
        filesize = os.stat(filename).st_size
        print 'created file - filename=%s filesize=%d' % (filename, filesize)
        
        return filename, filesize
    
    def _get_S3(self, bucket, filename):       
        key = Key(bucket)
        key.key = filename
        key.get_contents_to_filename(filename) 
              
    def _put_S3(self, bucket, filename):
        key = Key(bucket)
        key.key = filename
        key.set_contents_from_filename(filename)  
              
    def _delete_S3(self, bucket, filename):
        key = Key(bucket)
        key.key = filename
        key.delete()
    
    def connect(self):
       
        conn = S3Connection(self.access_key, self.secret_key,
            host=self.host)
        
        #print '\n'.join(i for i in dir(Location) if i[0].isupper())
        
        bucket = None
        
        try:
            bucket = conn.create_bucket(self.bucket)
            print 'created bucket %s' % self.bucket            
        except S3CreateError:
            bucket = conn.get_bucket(self.bucket)
            print 'got bucket %s' % self.bucket
        
        print bucket
            
        filename, filesize = self._create_file()
          
        print 'performing operation..(filesize=%d)' % filesize
        
        wrapped = None
        
        if self.op == 'GET':       
            print 'uploading %s to S3...' % filename                 
            self._put_S3(bucket, filename)
            print 'uploaded %s to S3...' % filename                                  
            wrapped = wrapper(self._get_S3, bucket, filename)
        elif self.op == 'PUT':
            wrapped = wrapper(self._put_S3, bucket, filename)
        elif self.op == 'DELETE':                 
            wrapped = wrapper(self._delete_S3, bucket, filename)  
        
        total_time = 0
        total_speed = 0
        
        min_speed = sys.maxint 
        max_speed = 0        
        
        for i in range(1, (self.numfiles+1) ):     
            
            if self.op == 'DELETE':
                self._put_S3(bucket, filename)

            time = timeit.timeit(wrapped, number=1) #self.numfiles)
            
            speed = (filesize / time) 

            total_time += time     
            total_speed += speed

            if speed < min_speed:
                min_speed = speed
            if speed > max_speed:
                max_speed = speed 
                        
            print 'i=%d time=%f speed=%f' % (i,time,speed) 
        
        avg_speed = total_speed / self.numfiles
        
        print 'total_time=%f avg_speed=%f min_speed=%f max_speed=%f' % ( total_time, avg_speed, min_speed, max_speed )
        
        conn.close()
    
        if self.clean_on_exit:
            os.remove(filename)
        
if __name__ == '__main__':
    
    parser = OptionParser(usage="s3performance is a simple tool to measure \
the performance of PUT, GET and DELETE commands to S3. Given \
the number and size of the files to perform one of the operations on, it will \
output the average, minimum and maximum time of each operation, operations \
per seconds and their speed in Mb/s. ")
    
    parser.add_option("-b", "--bucket", help="Bucket Name")
    parser.add_option("-o", "--operation", help="Values are PUT, GET and DELETE")
    parser.add_option("-n", "--numfiles", help="The number of files to perform operations on", type="int")
    parser.add_option("-s", "--size", help="The size of the files in KB", type="int")
    parser.add_option("-a", "--access_key", help="Access key")
    parser.add_option("-k", "--secret_key", help="Secret key")
    parser.add_option("-c", "--host", help="Host", default="demo")
    #parser.add_option('-u', '--chunk_size', help="The chunk size for multipart upload in KB.  Default is 50KB", type="int", default=(50 * 1024) )
    
    options, args = parser.parse_args()
    
    print options, args
    
    perf = S3Performance(options)
    
    #perf._create_file()
    perf.connect()


'''
sudo pip install FileChunkIO

'''
        
        
        