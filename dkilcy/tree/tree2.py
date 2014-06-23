'''
http://stackoverflow.com/questions/2482602/a-general-tree-implementation-in-python
'''

import uuid

def sanitize_id(id):
    return id.strip().replace(" ", "")

(_ADD, _DELETE, _INSERT) = range(3)
(_ROOT, _DEPTH, _WIDTH) = range(3)

class Node:

    def __init__(self, name, identifier=None, expanded=True):
        self.__identifier = (str(uuid.uuid1()) if identifier is None else
                sanitize_id(str(identifier)))
        self.name = name
        self.expanded = expanded
        self.__bpointer = None
        self.__fpointer = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def bpointer(self):
        return self.__bpointer

    @bpointer.setter
    def bpointer(self, value):
        if value is not None:
            self.__bpointer = sanitize_id(value)

    @property
    def fpointer(self):
        return self.__fpointer

    def update_fpointer(self, identifier, mode=_ADD):
        if mode is _ADD:
            self.__fpointer.append(sanitize_id(identifier))
        elif mode is _DELETE:
            self.__fpointer.remove(sanitize_id(identifier))
        elif mode is _INSERT:
            self.__fpointer = [sanitize_id(identifier)]

class Tree:

    def __init__(self):
        self.nodes = []

    def get_index(self, position):
        for index, node in enumerate(self.nodes):
            if node.identifier == position:
                break
        return index

    def create_node(self, name, identifier=None, parent=None):

        node = Node(name, identifier)
        self.nodes.append(node)
        self.__update_fpointer(parent, node.identifier, _ADD)
        node.bpointer = parent
        return node

    def show(self, position, level=_ROOT):
        queue = self[position].fpointer
        if level == _ROOT:
            print("{0} [{1}]".format(self[position].name, self[position].identifier))
        else:
            print("\t"*level, "{0} [{1}]".format(self[position].name, self[position].identifier))
        if self[position].expanded:
            level += 1
            for element in queue:
                self.show(element, level)  # recursive call

    def expand_tree(self, position, mode=_DEPTH):
        # Python generator. Loosly based on an algorithm from 'Essential LISP' by
        # John R. Anderson, Albert T. Corbett, and Brian J. Reiser, page 239-241
        yield position
        queue = self[position].fpointer
        while queue:
            yield queue[0]
            expansion = self[queue[0]].fpointer
            if mode is _DEPTH:
                queue = expansion + queue[1:]  # depth-first
            elif mode is _WIDTH:
                queue = queue[1:] + expansion  # width-first
    
    def is_branch(self, position):
        return self[position].fpointer

    def __update_fpointer(self, position, identifier, mode):
        if position is None:
            return
        else:
            self[position].update_fpointer(identifier, mode)

    def __update_bpointer(self, position, identifier):
        self[position].bpointer = identifier

    def __getitem__(self, key):
        return self.nodes[self.get_index(key)]

    def __setitem__(self, key, item):
        self.nodes[self.get_index(key)] = item

    def __len__(self):
        return len(self.nodes)

    def __contains__(self, identifier):
        return [node.identifier for node in self.nodes if node.identifier is identifier]

if __name__ == "__main__":
    import json
    
    tree1 = Tree()
    tree1.create_node("Root", "root")  # root node
    tree1.create_node({"foo":"a"}, "a", parent = "root")
    tree1.create_node({"foo":"b"}, "b", parent = "a")
    tree1.create_node({"foo":"c"}, "c", parent = "a")
    tree1.create_node({"foo":"d"}, "d", parent = "b")
    tree1.create_node({"foo":"e"}, "e", parent = "c")
    
    print("="*80)
    tree1.show("root")
    print("="*80)
    for node in tree1.expand_tree("root", mode=_WIDTH):
        print(node)
    print("="*80)
    
    # ===
        
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
       {'id':16, 'parent_id':None,  'a':'a16'},   

       ]
    
    tree2 = Tree()
    tree2.create_node("Root", "root")  # root node
    
    for d in data:
        id = d['id']
        parent_id = d['parent_id']
        if parent_id == None:
            parent_id = "root"        
        #print d, id, parent_id                
        tree2.create_node( d, identifier=str(id), parent=str(parent_id))
        
    print("="*80)    
    tree2.show("root")  
    print("="*80)
    
    print 'tree2.get_index(0): ', tree2.get_index(str(10))
    print 'tree2.get_index(1): ', tree2.get_index(str(12))
    
    for node in tree2.expand_tree(str(10), mode=_DEPTH):
        print type(tree2[node]), tree2[node].name, tree2[node].identifier
        
    print("="*80)
    
    '''   
    for node in tree2.expand_tree("root", mode=_DEPTH):
        print(node)
    print("="*80)
    
    for node in tree2.expand_tree("root", mode=_WIDTH):
        print(node)
    print("="*80)
    '''

    