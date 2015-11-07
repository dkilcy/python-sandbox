import os
access_key=os.environ['RS2_ACCESS_KEY']
secret_key=os.environ['RS2_SECRET_KEY']

from boto.s3.connection import S3Connection
conn = S3Connection(access_key,secret_key,host='demo.scality.com')

###

bucket = conn.create_bucket('tstest1-b1')
#bucket = conn.get_bucket('tstest1-b1')

print bucket.list()
for c in bucket.list():
   print c

print conn.get_all_buckets()

for b in conn.get_all_buckets():
   print b

#bucket.set_acl('public-read')

###

from boto.s3.key import Key
k = Key(bucket)
k.key = 'test1.dat'
k.set_contents_from_string('hello123')
#k.set_acl('public-read')


c = Key(bucket)
c.key = 'test1.dat'
print c.get_contents_as_string()
print c.get_acl()
###

###

full_bucket = conn.get_bucket('tstest1-b1')
# It's full of keys. Delete them all.
for key in full_bucket.list():
    key.delete()

# The bucket is empty now. Delete it.
conn.delete_bucket('tstest1-b1')

###

from boto.s3.connection import Location
print '\n'.join(i for i in dir(Location) if i[0].isupper())

