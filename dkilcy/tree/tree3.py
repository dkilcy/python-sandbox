
from treelib import Tree, Node

import json
import pprint

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

   {'id':10, 'parent_id':None,  'a':'a10'},
   {'id':11, 'parent_id':10,    'a':'a11'},
   {'id':12, 'parent_id':10,    'a':'a12'},        
   {'id':13, 'parent_id':11,    'a':'a13'},
   {'id':14, 'parent_id':12,    'a':'a14'},
   {'id':15, 'parent_id':None,  'a':'a15'},
   #{'id':16, 'parent_id':None,  'a':'a16'},   

   ]

tree = Tree()
tree.create_node("Root", "root")  # root node

for d in data:
    id = d['id']
    parent_id = d['parent_id']
    if parent_id == None:
        parent_id = "root"        
    print d, id, parent_id             
    tree.create_node( tag=str(id), identifier=str(id), parent=str(parent_id), data=d)  # tag=str(d),

tree.show()

print type(tree.to_dict())
print tree.to_dict()

#print json.dumps(tree.to_json())
print json.dumps(tree.to_dict())

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(json.loads(tree.to_json()))
    
    
