
from datetime import datetime, timedelta

now = datetime.now()
before = now - timedelta(minutes=+15)

format = "%Y-%m-%dT%H:%M:%S"
end_time = now.strftime(format)
start_time = before.strftime(format)

print start_time, end_time

data = {
  'filter': "{\"and\": [{\">\":{\"timestamp\":\"%s\"}},{\"<\":{\"timestamp\":\"%s\"}}]}" % (start_time, end_time)         
}

print data
print data['filter']       
        
        