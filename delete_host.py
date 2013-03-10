#!/usr/bin/env python
import sys

from api import task
import hub.lib.error as error

import salt.client

# To be replaced with proper config
# in the meantime, create your own tempconfig (keep out of Git)
import tempconfig
salt_master_conf = tempconfig.salt_master_conf
salthost = tempconfig.host_salthost

# Initiate salt client
client = salt.client.LocalClient(salt_master_conf)

@task
def delete_host(input):
    print('My input is {0}'.format(input))
    org = input['org']
    hostname = input['hostname']
    result = client.cmd(salthost, 'host.host_delete', [org, hostname])
    if result[salthost]['exit_code'] != 3:
        raise error.HubError(result)
    return result[salthost]
