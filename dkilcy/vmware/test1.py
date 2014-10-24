import argparse
from sys import exit

from pysphere import VIServer, VITask, MORTypes
from pysphere.resources import VimService_services as VI

server = VIServer()
server.connect('38.90.141.145', 'cred_user', 'xx')

for vm_name in server.get_registered_vms():
    vm = server.get_vm_by_path(vm_name)
    pm = server.get_performance_manager()
    print dir(pm)
    print dir(pm.INTERVALS)
    print pm.get_entity_counters.func_code.co_varnames
#    exit()
    res = pm.get_entity_counters(vm._mor, interval=pm.INTERVALS.CURRENT)
#    res = pm.get_entity_counters(vm._mor, interval=pm.INTERVALS.PAST_DAY)

    if res:
        for k, v in res.iteritems():
            print k, '=>', v
            '''
            if 'write' in k.lower():
                print k, '=>', v
            elif 'read' in k.lower():
                print k, '=>', v
            '''

        print '*** VM Name:', vm.get_property('name')
        counters = dict(
            cpu_usage=2,
            cpu_usage_mhz=6,
            cpu_used=14,
            mem_usage=24,
            net_recv=148,
            net_sent=149,
            disk_read=171,
            disk_write=173,
            )
#        stats = pm.get_entity_statistic(vm._mor, [2, 24, 6, 149])
        stats = pm.get_entity_statistic(vm._mor, [v for k, v in counters.iteritems()])
        for s in stats:
            print '*** %s: %s (%s)' % (s.group, s.value, s.unit)
            print s.counter, s.description, s.value, s.time, s.group, s.unit

        break

server.disconnect()

