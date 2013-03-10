#!/usr/bin/env python

from api import task
import hub.lib.error as error
import salt.client
import sys

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf
salthost = tempconfig.host_salthost

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)

@task
def create_host(data):
    uuid = data['uuid']
    org = data['org']
    network_type = data['network_type']
    storage_type = data['storage_type']
    vm_family = data['vm_family']
    vm_type = data['vm_type']
    mem = data['mem']
    cpu = data['cpu']
    hostname = org + '-' + str(uuid)
    
    result = client.cmd(salthost, 'host.host_create', [org, hostname, uuid, mem, cpu, vm_family, vm_type, storage_type, network_type])
    if result[salthost]['exit_code'] != 0:
        raise error.HubError(result)
    data['hostname'] = hostname
    return data
