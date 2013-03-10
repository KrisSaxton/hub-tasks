#!/usr/bin/env python

from api import task
import hub.lib.error as error
import salt.client

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf
salthost = tempconfig.dhcp_salthost

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)

@task
def search_dhcp(data):
    hostname = data['hostname']
    result = client.cmd(salthost, 'dhcp.reservation_search', [hostname])
    if result[salthost]['exit_code'] != 0:
        raise error.HubError(result)
    data['mac'] = result[salthost]['data'][0][1]['dhcpHWAddress'][0].split(' ')[1]
    data['ip'] = result[salthost]['data'][0][1]['dhcpStatements'][0].split(' ')[1]
    return data
