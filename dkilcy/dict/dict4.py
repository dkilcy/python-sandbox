
class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

items = {}

def _recurse(detail, count=1):
    
    result = AutoVivification()
    
    for d in data:
        parent_id = d.get('parent_id')
        if parent_id:
            pass
            
    return result
    
    
if __name__=='__main__':
    import json
    
    a = AutoVivification()

    a[1][2][3] = 4
    a[1][3][3] = 5
    a[1][2]['test'] = 6
    
    print a

    data = [
       {'id':10, 'parent_id':None,  'a':'a10'},
       {'id':11, 'parent_id':10,    'a':'a11'},
       {'id':12, 'parent_id':10,    'a':'a12'},        
       {'id':13, 'parent_id':11,    'a':'a13'},
       {'id':14, 'parent_id':12,    'a':'a14'},
       {'id':15, 'parent_id':None,  'a':'a15'},
       {'id':16, 'parent_id':None,  'a':'a16'},   
       ]
    
    for d in data:
        d[data['id']] = data
    
    l = json.dumps(data)    # JSON to Python
    o = json.loads(l)
    
    print type(data)
    print type(l)
    print type(o)
    
    b = AutoVivification()
    
    
    
    