# http://www.quesucede.com/page/show/id/python-3-tree-implementation
# Brett Kromkamp (brett@youprogramming.com)
# You Programming (http://www.youprogramming.com)
# May 03, 2014

(_ROOT, _DEPTH, _BREADTH) = range(3)

class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children

    def add_child(self, identifier):
        self.__children.append(identifier)
        
class Tree:

    def __init__(self):
        self.__nodes = {}

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self[identifier] = node

        if parent is not None:
            self[parent].add_child(identifier)

        return node

    def display(self, identifier, depth=_ROOT):
        children = self[identifier].children
        if depth == _ROOT:
            print("{0}".format(identifier))
        else:
            print("t"*depth, "{0}".format(identifier))

        depth += 1
        for child in children:
            self.display(child, depth)  # recursive call

    def traverse(self, identifier, mode=_DEPTH):
        # Python generator. Loosly based on an algorithm from 
        # 'Essential LISP' by John R. Anderson, Albert T. Corbett, 
        # and Brian J. Reiser, page 239-241
        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0]
            expansion = self[queue[0]].children
            if mode is _DEPTH:
                queue = expansion + queue[1:]  # depth-first
            elif mode is _BREADTH:
                queue = queue[1:] + expansion  # width-first

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item

if __name__=='__main__':
    import json
    
    tree = Tree()
    
    tree.add_node("A")  # root node
    tree.add_node("B", "A")
    tree.add_node("C", "A")
    tree.add_node("D", "B")
    tree.add_node("E", "C")
    
    tree.display("A")

    for node in tree.traverse("A", mode=_BREADTH):
        print(node)
    
    #print json.dumps(tree)
        