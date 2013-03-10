#!/usr/bin/env python

from api import task
import hub.lib.error as error
import salt.client

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf
salthost = tempconfig.lvm_salthost

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)


@task
def create_lvm(data):
    hostname = data['hostname']
    storage_size = data['storage_size']
    result = client.cmd(salthost, 'lvm.create', [hostname, storage_size])    
    if result[salthost]['exit_code'] != 0:
        raise error.HubError(result)
    return data
