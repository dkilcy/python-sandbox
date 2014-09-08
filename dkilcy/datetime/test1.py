from datetime import date, datetime

start_time = 1406890260
end_time = 1409482260

now = datetime.now()

timestamp = int((now - datetime(1970, 1, 1)).total_seconds())

print start_time
print end_time
print timestamp

if start_time < timestamp < end_time:
    print "yes"
    
    
print now.date()

print datetime.fromtimestamp(timestamp)
