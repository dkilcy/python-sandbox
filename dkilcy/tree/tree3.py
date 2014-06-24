
from treelib import Tree, Node

import json
import pprint
import sys

def walk(node):
    results = [node['id']]
    
    if node.get('children'):
        for child in node['children']:
            results.extend(walk(child))
    return results

    
if __name__=='__main__':
    
    data = [
       #{'id':14, 'parent_id':12,    'a':'a14'},
       #{'id':15, 'parent_id':None,  'a':'a15'},       
    
       #{'id':20, 'parent_id':None,  'a':'a20'},
       #{'id':21, 'parent_id':20,    'a':'a21'},
       #{'id':22, 'parent_id':20,    'a':'a22'},        
       #{'id':23, 'parent_id':21,    'a':'a23'},
       #{'id':24, 'parent_id':22,    'a':'a24'},
       #{'id':25, 'parent_id':None,  'a':'a25'},
       #{'id':26, 'parent_id':None,  'a':'a26'}, 
    
       {'id':10, 'parent_id':None,  'a':'a10', 'b':'foooofodfds' },
       {'id':11, 'parent_id':10,    'a':'a11', 'b':'foooofodfds' },
       {'id':12, 'parent_id':10,    'a':'a12', 'b':'foooofodfds' },        
       {'id':13, 'parent_id':11,    'a':'a13', 'b':'foooofodfds' },
       {'id':14, 'parent_id':12,    'a':'a14', 'b':'foooofodfds' },
       {'id':15, 'parent_id':None,  'a':'a15', 'b':'foooofodfds' },
       {'id':16, 'parent_id':None,  'a':'a16', 'b':'foooofodfds' },   
    
       ]
    
    tree = Tree()
    tree.create_node("Root", "root")  # root node
    
    for d in data:
        id = d['id']
        parent_id = d['parent_id']
        if parent_id == None:
            parent_id = "root"        
        print d, id, parent_id             
        tree.create_node( identifier=str(id), parent=str(parent_id), data=d)  # tag=str(d),
    
    tree.subtree('10').show()
    
    print "get_node('10'):data", tree.get_node('10').data
    cs = tree.children('10')
    print "get_node('10').children:", cs
    for c in cs:
        print 'c:', c.data 
    
    print "get_node('14'):", tree.get_node('14').data
    
    all_nodes = tree.all_nodes()
    for node in all_nodes:
        print node.data
    
    #print type(tree.to_dict())
    out = tree.to_dict()
    print out
    
    for k,v in out.iteritems():
        print 'k:', k
        
    print 'out1: ', out
    
    sys.exit()

    print 'out2: ', out['Root']
    print 'out3: ', out['Root']['children']
    print 'out4: ', out['Root']['children'][0]
    
    print json.dumps(tree.to_json())
    #print json.dumps(tree.to_dict())
    
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(json.loads(tree.to_json()))
        
    subt = tree.subtree('root')
    print type(subt)
    
    cs = tree.siblings('10')
    print "cs: ", cs
    for c in cs:
        print 'c:', c.data 
    
    print "tree.get_node('10').data:", tree.get_node('10').data
    l =  walk(tree.get_node('10').data)
    print type(l)
    for x in l:
        print x
