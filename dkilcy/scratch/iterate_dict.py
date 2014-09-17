

dict = { "foo":"bar", "baz":"biz", "num":0 }

for k in dict:
    print k, dict[k]
    
    
p = {"description": "Sample paramiko description", "automation_type": "paramiko", "fields": {"run_script": "uptime"}, "is_archived": 0, "id": 1, "profile_url": "/automations/paramiko/1", "name": "Paramiko Test 1"}
    
fields = p.pop('fields')
for key in fields:
    print key, fields[key]
    #p[key] = fields[key]
    
print p
    