import json

def listToDict(input):
    
    root = {}
    lookup = {}
    lookup[0] = root
    
    for item in input:
        id = item.pop('id')
        parent_id = item.pop('parent_id')
        
        if parent_id == None:
            parent_id = 0; 
        
        node = {}
        node['id'] = id
        for k,v in item.iteritems(): 
            node[k] = v           
        
        lookup[parent_id].setdefault('children', []).append(node)
        lookup[id] = node
    
    return root

if __name__=='__main__':
    
    items = [
       {'id':11, 'parent_id':10,    'a':'a11', 'b':'foo1'},
       {'id':10, 'parent_id':None,  'a':'a10', 'b':'foo0'},
       #{'id':11, 'parent_id':10,    'a':'a11', 'b':'foo1'},
       {'id':12, 'parent_id':10,    'a':'a12', 'b':'foo2'},        
       {'id':13, 'parent_id':11,    'a':'a13', 'b':'foo3'},
       {'id':14, 'parent_id':12,    'a':'a14', 'b':'foo4'},
       {'id':15, 'parent_id':None,  'a':'a15', 'b':'foo5'},
       {'id':16, 'parent_id':None,  'a':'a16', 'b':'foo6'},   
       ]
    
    result = listToDict(items)
    
    print result
    print json.dumps(result)
