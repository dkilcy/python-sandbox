
# http://www.ssdfreaks.com/content/599/how-to-convert-mbps-to-iops-or-calculate-iops-from-mbs
# http://deangrant.wordpress.com/2012/02/11/a-calculation-for-mbps-to-iops-and-vice-versa/

'''
IOPS = (MBps throughput / KB per IO) * 1024 
MBps = (IOPS * KB per IO) / 1024
'''
def calc_MBps_IOPS(throughput, request_size):
    iops = ( float(throughput)/ float(request_size)) * 1024
    print 'iops=%0.4f' % (iops) 
    
    throughput = (iops * float(request_size)) / 1024
    print 'XXps=%0.4f' % (throughput) # 10

# -------------------------------------------------------------------------- #

'''
calc_MBps_IOPS(throughput=10.0, request_size=8.0)# IOPS = 1280, MBps = 10
calc_MBps_IOPS(throughput=10000.0, request_size=8000.0)# IOPS = 1280, Bps=10000
calc_MBps_IOPS(throughput=76.2, request_size=4.0)
'''
    
# Mbps, Mbytes
'''
throughput is 4.20 Mb/s 
Convert 5242880 bytes to Kb
'''
x = float(5242880 * 8) / 1024 

calc_MBps_IOPS(throughput=4.20, request_size=x) # IOPS=0.1050  Mbps=4.20

bytes1 = float(10240)

kilobits1 = (bytes1 * 8) / 1024
kilobytes1 = bytes1 / 1024

megabits1 = (bytes1 * 8) / 1024 / 1024
megabytes1 = (bytes1) / 1024 / 1024

gigabits1 = (bytes1 * 8) / 1024 / 1024 / 1024
gigabytes1 = bytes1 / 1024 / 1024 / 1024

terabits1 = (bytes1 * 8) / 1024  / 1024 / 1024 / 1024
terabytes1 = bytes1 / 1024  / 1024 / 1024 / 1024

petabytes1 = bytes1 / 1024 / 1024 / 1024 / 1024 / 1024

print kilobits1, kilobytes1, megabits1, megabytes1, gigabits1, gigabytes1, \
    terabits1, terabytes1, petabytes1
    
    

  