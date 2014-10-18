'''
pip install requests
pip install -U python-ceilometerclient
'''

import json
import requests

from ceilometerclient import client

controller = 'controller-01.mgmt'
username = 'admin'
password = '94bcee677185fee9c0bf'
tenantName = 'admin'

payload = {'auth': {'tenantName': tenantName, 'passwordCredentials': {'username': username, 'password': password}}}

res = requests.post('http://%s:5000/v2.0/tokens' % (controller), 
   headers={'content-type': 'application/json'},
   data=json.dumps(payload))

print res


