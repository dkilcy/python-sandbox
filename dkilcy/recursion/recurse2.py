

def do_work():

    d = {"id":10, "a":"a10"}
    
    result = _do_work_recurse(d)[0]
    return result

def _do_work_recurse(data, count=1):
    
    id = data.get('id')
    
    end = 1
    result = []
    
    for x in range(0,end):
        print x
        temp_result = None
        result.append(temp_result)
        
    return result
    
    
if __name__=='__main__':
    import json
    
    result = do_work()
    
    print json.dumps(result)