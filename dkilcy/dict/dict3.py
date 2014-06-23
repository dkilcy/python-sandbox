#!/usr/bin/python

import json

def main():
    data = '[{"id":10, "parent_id":null, "a":"a10"}, {"id":11, "parent_id":10, "a":"a11"}, {"id":12, "parent_id":10, "a":"a12"} ]'
       
    j = json.loads(data)
    #json_string = json.dumps(j,sort_keys=True,indent=2)
    #print json_string
    
    print j
    print json.dumps(j)
    
    d = {}
    
    #parent =  j["id"]
    for item in j:
        #print item["a"]
        #print item["id"]
        #print item["parent_id"]        
        d[ item["id"] ] = item

    print 'j[0]=', j[0]     # j[0]= {u'a': u'a10', u'parent_id': None, u'id': 10}
    print 'd[10]=', d[10]   # d[10]= {u'a': u'a10', u'parent_id': None, u'id': 10}
    
    #for k,v in d.iteritems():
    #    print k,v   #10 {u'a': u'a10', u'parent_id': None, u'id': 10} ...

    #for item in j:
        
    
if __name__ == "__main__":   
    main()
    
    d = {}
    d['foo'] = 10
    d['bar'] = None
    
    print json.dumps(d)  # {"foo": 10, "bar": null}
    