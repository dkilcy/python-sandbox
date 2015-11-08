from SimpleXMLRPCServer import SimpleXMLRPCServer
import pprint

# Create server
server = SimpleXMLRPCServer(("conn2.mgmt", 8000))
server.register_introspection_functions()

# struct(status, user(id, privatekey, displayname, enabled, bucketnrlimit, bucketsizelimit, requestlimit))
def getUserSecretKey(user):
    print user
    if user == "scalityrs2":
        print "Found ", user
        return {"status" : True,
            "user" : {
                "id" : "54EE2BA8C3072DB154EE2B000000004000000140",
                "privatekey" : "secretkey",
                "displayname" : "scalityrs2",
                "enabled" : True,
                "bucketnrlimit" : 100,
                "bucketsizelimit" : -1,
                "requestlimit" : -1
            }
            }
    else:
        print "Not found"
        return {"status" : False, "user" : {}}

server.register_function(getUserSecretKey)

#updateBucketStorage(array(struct(bucketOwnerId, bucketOwnerName, bucket, bucketName, fullVolume, timestamp)))
def updateBucketStorage(items):
    print "updateBucketStorage"
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(items)
    return True
server.register_function(updateBucketStorage)

# addBucketDownload(array(struct(requesterId, requesterName, bucketOwnerId, bucketOwnerName, bucket, bucketName, type, volume)))
def addBucketDownload(items):
    print "addBucketDownload"
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(items)
    return True
server.register_function(addBucketDownload)

# addBucketUpload(array(struct(requesterId, requesterName, bucketOwnerId, bucketOwnerName, bucket, bucketName, type, volume)))
def addBucketUpload(items):
    print "addBucketUpload"
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(items)
    return True
server.register_function(addBucketUpload)

# addBucketRequest(array(struct(requesterId, requesterName, bucketOwnerId, bucketOwnerName, bucket, bucketName, type, number)))
def addBucketRequest(items):
    print "addBucketRequest"
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(items)
    return True
server.register_function(addBucketRequest)



# Run the server's main loop
server.serve_forever()

