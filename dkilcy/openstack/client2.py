#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://ask.openstack.org/en/question/49962/how-to-fetch-metric-values-with-the-python-api/
https://github.com/openstack/python-ceilometerclient/blob/master/ceilometerclient/client.py

/etc/ceilometer/pipeline.yaml
'''

from ceilometerclient import client
from os import environ as env
from ceilometerclient.common import utils

keystone = {}
keystone['os_username']=env['OS_USERNAME']
keystone['os_password']=env['OS_PASSWORD']
keystone['os_auth_url']=env['OS_AUTH_URL']
keystone['os_tenant_name']=env['OS_TENANT_NAME']

#creating an authenticated client
ceilometer_client = client.get_client(2,**keystone)

#now you should be able to use the API

for sample in ceilometer_client.samples.list(meter_name='cpu_util',limit=10,
    q=[
        {'field': 'timestamp', 'op': 'gt', 'value': '2014-10-17T00:00:00'}, 
        {'field': 'timestamp', 'op': 'lt', 'value': '2014-10-17T00:10:00'}, 
    ]):
    print sample.timestamp, sample.resource_id, sample.counter_name, sample.counter_volume



