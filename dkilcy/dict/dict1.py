'''

'''

import json
    
def do_work(nodes):    
    ##print nodes[0]    
    results = []    
    
    d = {}
    for node in nodes:
        d[node['id']] = []
        
    for node in nodes:
        #print 'type(node):', type(node)  # <type 'dict'>
        if node.get('parent_id'):                                          
            #obj1 = json.dumps(node)            
            #print 'obj1:', obj1, type(obj1) # <type 'str'>                       
            #obj2 = json.loads(obj1);
            #print 'obj2:', obj2, type(obj2) # <type 'dict'>                       
            id = node['id']
            parent_id = node['parent_id']            
            #print id, parent_id                            
            d[parent_id].append(id)            
            print 'd:', d     
       
    return d

if __name__=='__main__':
    import pprint
    
    # list of dictionaries
    data = [
       {'id':10, 'a':'a1', 'b':1 },
       {'id':11, 'parent_id':10, 'a':'a1', 'b':1 },
       {'id':12, 'parent_id':10, 'a':'a1', 'b':1 },        
       {'id':13, 'parent_id':11, 'a':'a1', 'b':1 },
       {'id':14, 'parent_id':12, 'a':'a1', 'b':1 }  
       ]
    
    print type(data) # <type 'list'>
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)    
    print 'json.dumps(data):', json.dumps(data)
    
    result = do_work(data)    
    pp.pprint(result)
    print 'json.dumps(result):', json.dumps(result)
    