__author__ = 'Change'

#!/usr/bin/python

from get_sys_info import GetSysInfo
import os
from random import sample

sys_info = GetSysInfo()

disks_dict = sys_info.get_disks_dict()

for key,value in disks_dict.iteritems():
    if len(value) > 28:
        for i in xrange(1,4):
            random_disk = sample(value,9)
            disk_group = ' '.join(random_disk)
            print disk_group
            command = 'ucli dg_create -d vg' + str(i) +' -t 5 -n 9 ' + disk_group + ' -f 0 -s 64 -m 200'
            print command
            os.system(command)
            for disk in random_disk:
                value.remove(disk)
