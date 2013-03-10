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
def delete_vm(data):
    hostname = data['hostname']
    result = client.cmd(salthost, 'vm.store_delete', [hostname])
    if result[salthost]['exit_code'] != 3:
            raise error.HubError(result)
    return result[salthost]
