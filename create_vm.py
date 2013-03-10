#!/usr/bin/env python

from api import task
import hub.lib.error as error
import salt.client

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf
salthost = tempconfig.vm_salthost

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)


@task
def create_vm(data, install):
    uuid = data['uuid']
    hostname = data['hostname']
    mem = data['mem']
    cpu = data['cpu']
    vm_family = data['vm_family']
    network_type = data['network_type']
    storage_type = data['storage_type']

    result = client.cmd(salthost, 'vm.store_create', [vm_family, hostname, uuid, mem, cpu, storage_type, network_type, install])
    if result[salthost]['exit_code'] != 0:
        raise error.HubError(result)
    return data
