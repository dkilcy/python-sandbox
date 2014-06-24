

if __name__=='__main__':
    
    item_list = [
       {'id':10, 'parent_id':None,  'a':'a10'},
       {'id':11, 'parent_id':10,    'a':'a11'},
       {'id':12, 'parent_id':10,    'a':'a12'},        
       {'id':13, 'parent_id':11,    'a':'a13'},
       {'id':14, 'parent_id':12,    'a':'a14'},
       {'id':15, 'parent_id':None,  'a':'a15'},
       {'id':16, 'parent_id':None,  'a':'a16'},   
       ]
    
    items_by_id = {i.id:i for i in item_list}
    parents = []
    
    for i in item_list:
        i.__dict__.setdefault('_children', [])  # ensures that all items have a children list even if it is empty
        if i.parent_id:
            parent = items_by_id[i.parent_id]
            parent.__dict__.setdefault('_children', []).append(i)
        else:
            parents.append(i) 
            