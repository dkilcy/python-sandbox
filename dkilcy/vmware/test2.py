import sys

from pprint import pprint
from pysphere import VIServer

password = sys.argv[1]

server = VIServer()
server.connect('38.90.141.145', 'cred_user', password)

hosts = server.get_hosts() #returns dictionary with host MORs and names
print hosts, hosts.items()
#host = [k for k,v in hosts.items() if v == 'myesx1.example.com'][0]

pm = server.get_performance_manager()

for host in hosts:
    print host
    
    entity_counters = pm.get_entity_counters(host, interval=None)
    print entity_counters
    
    counters = [2,24]    
    statistics = pm.get_entity_statistic(host, counters, interval=pm.INTERVALS.PAST_DAY, composite=False)
    print statistics
    
    for s in statistics:
        print "counter='%s' description='%s' value='%s' time='%s' group='%s' group_description='%s' unit='%s' unit_description='%s' " \
             % (s.counter, s.description, s.value, s.time, s.group, s.group_description, s.unit, s.unit_description)
    
vm_paths = server.get_registered_vms() #datacenter, cluster, resource_pool, status, advanced_filters)
for vm_path in vm_paths:
    #print type(vm_path)
        
    print vm_path
    vm = server.get_vm_by_path(vm_path) #datacenter=None
    print vm.get_status()
    pprint(vm.get_properties(from_cache=False))



    