#!/usr/bin/env python

from api import task
import salt.client
import sys

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf
salthost = tempconfig.ip_salthost

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)


@task
def release_ip(data):
    network_id = data['network_id']
    network_mask = data['network_mask'] 
    ip = data['ip']
    result = client.cmd(salthost, 'ip.release', [network_id, network_mask, ip])
    if result[salthost]['exit_code'] != 0:
        raise error.HubError(result)
    ip = result[salthost]['data'][0]
    return data
