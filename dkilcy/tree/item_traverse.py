
import json
    
from dkilcy.tree.tree1 import Tree
        
def find_children(nodes):

    d = {}
    for node in nodes:
        d[node['id']] = []
        
    for node in nodes:
        if node.get('parent_id'):                                                           
            id = node['id']
            parent_id = node['parent_id']                                   
            d[parent_id].append(id)            
            #print 'd:', d     
    return d
    
if __name__=='__main__':

    data = [
       {'id':10, 'parent_id':None,  'a':'a10'},
       {'id':11, 'parent_id':10,    'a':'a11'},
       {'id':12, 'parent_id':10,    'a':'a12'},        
       {'id':13, 'parent_id':11,    'a':'a13'},
       {'id':14, 'parent_id':12,    'a':'a14'},
       {'id':15, 'parent_id':None,  'a':'a15'},
       {'id':16, 'parent_id':None,  'a':'a16'},   
       ]
    
    print 'json.dumps(data):', json.dumps(data)
    
    items = find_children(data)
    print 'json.dumps(items):', json.dumps(items)
    
    keys = []
    for k,v in items.iteritems():
        print "key,values:", k,v
        keys.append(k)
        
    (_ROOT, _DEPTH, _BREADTH) = range(3)
    
    tree = Tree()

    tree.add_node("root")  # root node
    
    temp = []

    # make a list of parents with no children
    for k,v in items.iteritems():
        if len(v) == 0:
            temp.append(k)
            tree.add_node(k, "root")            
    
    for k,v in items.iteritems():
        if len(v) > 0:
            for x in v:
                print k,x
                try:
                    tree.add_node(x,k)
                    #print 'adding(1): ', k, x                
                except KeyError:
                    #print 'adding(2): ', k, x
                    tree.add_node(k, "root")
                    tree.add_node(x, k)
                
        #else:
        #    tree.add_node(k, "root")
        #    tree.add_node(x, k)
               
    tree.display("root")

    #for node in tree.traverse(10, mode=_BREADTH):
    #    print(node)
        
        