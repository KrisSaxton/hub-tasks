#!/usr/bin/env python

from api import task
import salt.client
import sys

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)

@task
def catlogue(data):
    try:
        size = data['size']:
    except KeyError
        size = 'small'
    if size == 'small':
        data['cpu'] = '1'
        data['mem'] = '512'
        data['storage_size'] = 20
    elif size == 'medium'
        data['cpu'] = '1'
        data['mem'] = '1024'
        data['storage_size'] = 40
    elif size == 'large'
        data['cpu'] = '2'
        data['mem'] = '2048'
        data['storage_size'] = 60
    elif size == 'vlarge'
        data['cpu'] = '2'
        data['mem'] = '4096'
        data['storage_size'] = 60
    return data    
