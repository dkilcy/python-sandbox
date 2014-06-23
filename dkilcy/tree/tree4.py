import collections
import json

def Tree():
    return collections.defaultdict(Tree)

t = Tree()

t['id'] = {"id":10 }
t[0][0] = {"children":[]}


print json.dumps(t)