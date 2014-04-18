import sys 

role = sys.argv[1] 

def comp_split(role):
    parts = role.split('.')
    if len(parts) == 1 :
        service_name = parts[0]
        deployment_name = None
        role_name = None
    elif len(parts) == 2:
        service_name, deployment_name = parts
        role_name = None
    elif len(parts) == 3:
        service_name, deployment_name, role_name = parts

    return len(parts), service_name, deployment_name, role_name

i, service_name, deployment_name, role_name = comp_split(role) 

print service_name
print deployment_name
print role_name

if i == 1:
    print 'cloud'
elif i == 2:
    print 'depl'
elif i == 3:
    print 'role'

##############################################################################

for slot in 'production','staging':
    print slot

##############################################################################

#args = {u'flavorRef': u'1', u'network-nova': u'34882d4f-0363-49ed-9ef5-317481a2db4c', u'region': u'RegionOne', u'imageRef': u'14ecd3ad-4430-4899-8d8d-3d3f6ed440ca', u'name': u'dkilcy-test5'}
#args = {u'flavorRef': u'1', u'network-neutron': u'00000-00000', u'region': u'RegionOne', u'imageRef': u'14ecd3ad-4430-4899-8d8d-3d3f6ed440ca', u'name': u'dkilcy-test5'}
#args = {u'flavorRef': u'1', u'network-nova': u'34882d4f-0363-49ed-9ef5-317481a2db4c', u'network-neutron': u'00000-00000', u'region': u'RegionOne', u'imageRef': u'14ecd3ad-4430-4899-8d8d-3d3f6ed440ca', u'name': u'dkilcy-test5'}
args = {u'flavorRef': u'1', u'region': u'RegionOne', u'imageRef': u'14ecd3ad-4430-4899-8d8d-3d3f6ed440ca', u'name': u'dkilcy-test5'}

network_nova = args.pop('network-nova', None)
network_neutron = args.pop('network-neutron', None)

list = []

if network_nova != None:
    list.extend([ {'uuid':network_nova } ])

if network_neutron != None:
    list.extend([ {'port':network_neutron } ])

if len(list) > 0: 
    args['networks'] = list

print args

##############################################################################

"""
*args and **kwargs
"""

def test_var_args(farg, *args):
    print("formal arg: %s" % farg)
    for arg in args:
        print("arg: %s" % arg);

test_var_args(1,2,3)
"""
formal arg: 1
arg: 2
arg: 3
"""

def test_var_kwargs(farg, **kwargs):
    print("formal arg: %s" % (farg))
    for key in kwargs:
        print("keyword arg: %s %s" % ( key, kwargs[key] ) )

test_var_kwargs(1, myarg1=1, myarg2="foo")
"""
formal arg: 1
keyword arg: myarg1 1
keyword arg: myarg2 foo
"""
 
def test_var_args_call(a,b,c):
    print("arg1: %s" % a)
    print("arg2: %s" % b)
    print("arg3: %s" % c)

varargs = {"c":1, "b":2}
test_var_args_call(3, **varargs)
"""
arg1: 3
arg2: 2
arg3: 1
"""

