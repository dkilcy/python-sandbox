
def work(node):
    for element in node:
        if 'parent' in element:
            if 'children' not in node[element['parent']]:
                node[element['parent']]['children'] = []
            node[element['parent']]['children'].append(element)
            del element['parent']

if __name__=='__main__':
    
    node = {}
    
    node[0]=[{"name":"RootNode"}]
    node[1]=[{"parent":0, "name":"country"}]
    node[2]=[{"parent":1, "name":"day"}]
    
    for k,v in node.iteritems():
        print k,v
        
    for element in node:
        if 'parent' in element:
            if 'children' not in node[element['parent']]:
                node[element['parent']]['children'] = []
            node[element['parent']]['children'].append(element)
            del element['parent']

    print node[0]