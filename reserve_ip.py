#!/usr/bin/env python

from api import task
import hub.lib.error as error
import salt.client

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf
salthost = tempconfig.ip_salthost

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)


@task
def reserve_ip(data):
    network_id = data['network_id']
    network_mask = data['network_mask']
    result = client.cmd(salthost, 'ip.reserve', [network_id, network_mask, 1])
    if result[salthost]['exit_code'] != 0:
        raise error.HubError(result)
    data['ip'] = result[salthost]['data'][0]
    return data
