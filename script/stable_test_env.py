#!/usr/bin/python
# -*- coding:utf-8 -*-

from sys_cli import SysCli
from cont_var import DG_NAMES as dg_names,DG_NAMES_NAS as dg_names_nas,IP_ADDRESS as ip_address

for dg_name_iscsi in dg_names_iscsi:
    for i in xrange(1,6):
        iscsi_vd_name = dg_name_iscsi + 'iscsi' + str(i)
        iscsi_sys_cli = SysCli(dg_name_iscsi,iscsi_vd_name,ip_address)
        iscsi_sys_cli.CreateIscsiLun()
        iscsi_sys_cli.IscsiLunAddPermission()

for dg_name_nas in dg_names_nas:
    for i in xrange(1,2):
        nas_vd_name = dg_name_nas + 'nas' + str(i)
        nas_sys_cli = SysCli(dg_name_nas,nas_vd_name,ip_address)
        nas_sys_cli.CreateNasLun()
        nas_sys_cli.CreateNasShare()
        nas_sys_cli.AddNfsAccessPermission()

