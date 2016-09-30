__author__ = 'Change'

import os,sys
import commands

disks_info = os.system("ucli sys_get_disk_info")

disks_info = disks_info.split('=====================================')

unconf_disks = {}

find_str = 'Belongs_to_DG:UNCONF'

for disk_info in disks_info:
    disk_info = disk_info.replace(' ','')
    disk_info = disk_info.split('\n')

    if find_str in disk_info:
        for info in disk_info:
            if info.startswith('Port_id'):
                value = info[8:]

            if info.startswith('Size(MB):'):
                key = info[10:]

        if unconf_disks.has_key(key):
            unconf_disks[key].append(value)

        else:
            unconf_disks[key] = []
            unconf_disks[key].append(value)


print unconf_disks