import json

def find_children_from_list(nodes):
    '''
    d['id']=1
    d['children']=[]
    d['children'].append({'id':12})
    d['children'].append({'id':13})
    print json.dumps(d) #{"id": 1, "children": [{"id": 12}, {"id": 13}]}
    '''
    x = {}

    for node in nodes:
        id = node['id']
        parent_id = node.get('parent_id')        
        
        if parent_id == None:
            continue
        
        x[parent_id]=[]
        
    for node in nodes:       
        id = node['id']
        parent_id = node.get('parent_id')
       
        if parent_id == None:
            continue
        
        # copy over all the key values
        d = {}
        for k, v in node.iteritems():
            d[k]=v
        d['id'] = id
        del d['parent_id']
        
        x[parent_id].append(d)

    return x
    
if __name__=='__main__':
    import pprint
    
    nodes = [
       {'id':10, 'parent_id':None,  'a':'a10'},
       {'id':11, 'parent_id':10,    'a':'a11'},
       {'id':12, 'parent_id':10,    'a':'a12'},        
       {'id':13, 'parent_id':11,    'a':'a13'},
       {'id':14, 'parent_id':12,    'a':'a14'},
       {'id':15, 'parent_id':None,  'a':'a15'},
       {'id':16, 'parent_id':None,  'a':'a16'},   
       ]
    
    print 'json.dumps(nodes):', json.dumps(nodes)
    
    #for node in nodes:
    result = find_children_from_list(nodes)
    #print result.items()
    #print result.values()
    
    print 'result: ', result
    
    keys = []
    for k,v in result.iteritems():
        print "key,values:", k,v
        keys.append(k)
    #print type(result) # <type 'dict'>
    
    print 'key list: ', keys
    #for key in keys:
    #    print key
                   
                   
    for d in nodes:
        id = d.get('id')
        #print id, result.get(id)
        r = result.get(id)
        if r != None:
            d['children'] = r
        del d['parent_id']
    
    print 'json.dumps(nodes):', json.dumps(nodes)
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(nodes)
    
    