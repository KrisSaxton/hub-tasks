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
def create_dhcp(ip_data, host_data):
    hostname = host_data['hostname']
    mac = host_data['mac']
    ip = ip_data['ip']
    result = client.cmd(salthost, 'dhcp.reservation_create', [hostname, mac, ip])
    if result[salthost]['exit_code'] != 0:
        raise error.HubError(result)
    data = dict(ip_data.items() + host_data.items())
    return data
