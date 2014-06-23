'''
A simple example that just walks the tree
'''

def recurse(node):

    results = []
    results.append(node['id'])
   
    #print results
    if len(node['children']) > 0:
        for child in node['children']:
            results.extend(recurse(child))    
    return results

if __name__=='__main__':
    
    data = {'id':'1','children':[
               {'id':'1-1','children':[
                     {'id':'1-1-1','children':[]},
                     {'id':'1-1-2','children':[]}
               ]},
               {'id':'1-2','children':[]}  ]}
    
    result = recurse(data)    
    print result
    