#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

class SysCli(object):
    def __init__(self,dg_name,*avgs):
        self.dg_name = dg_name

        if len(avgs) != 0:
            self.vd_name = avgs[0]
            self.ip_address = avgs[1]

    def create_iscsi_lun(self):
        create_iscsi_lun_CLI = 'ucli vd_iscsi -C -d ' + self.dg_name + ' -v ' + self.vd_name + ' -s 200000'
        os.system(create_iscsi_lun_CLI)

    def create_nas_lun(self):
        create_nas_lun_CLI = 'ucli vd_nas -C -d ' + self.dg_name + ' -v ' + self.vd_name + ' -s 200000'
        os.system(create_nas_lun_CLI)

    def del_iscsi_lun(self):
        del_iscsi_lun_CLI = 'ucli vd_iscsi -D -d ' + self.dg_name + ' -v ' + self.vd_name
        os.system(del_iscsi_lun_CLI)

    def del_nas_lun(self):
        del_nas_lun_CLI = 'ucli vd_nas -D -d ' + self.dg_name + ' -v ' + self.vd_name
        os.system(del_nas_lun_CLI)

    def iscsi_lun_add_permission(self):
        iscsi_lun_add_permission = 'ucli iscsi_access -A -d ' + self.dg_name + ' -v ' + self.vd_name + ' -i ' + self.ip_address
        os.system(iscsi_lun_add_permission)

    def create_nas_share(self):
        create_nas_share = 'ucli nas_share --create -n nasshre' + self.vd_name + ' -v ' + self.vd_name
        os.system(create_nas_share)

    def add_nfs_access_permission(self):
        add_nfs_access_permission = 'ucli nfs_access --add -p /share/' + self.vd_name + ' -i ' + self.ip_address + '-o rw,sync,nohide'
        os.system(add_nfs_access_permission)

    def del_dg(self):
        del_dg = 'ucli dg_delete -d '+ self.dg_name
        os.system(del_dg)