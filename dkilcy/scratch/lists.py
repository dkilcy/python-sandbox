

project_ids = []
whitelist = [2,4]

for i in project_ids:
    print i
for i in whitelist:
    print i
    
s1 = set(project_ids)
s2 = set(whitelist)

print s1
print s2

i1 = list(s1.intersection(s2))
print i1

i2 = list(s1.union(s2))
print i2

i3 = list(s1.difference(s2))
print i3

print "index(4): ", whitelist.index(4)
print whitelist.index(0)

op=None

if op is not None:
    if op != 'stop' and op != 'terminate':
        print 'err1'
    else:
        print 'ok'
    