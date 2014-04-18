'''
Created on Apr 17, 2014

@author: dkilcy
'''
import sys
import pymongo

conn = pymongo.MongoClient("mongodb://localhost")

db = conn.test
users = db.users

doc = { "_id":1, "firstname":"David","lastname":"Kilcy"}
print doc

try:
    users.insert(doc)
except:
    print "insert failed:", sys.exc_info()
    
    