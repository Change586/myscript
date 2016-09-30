#!/usr/bin/python
# -*- coding:utf-8 -*-

from sys_cli import Sys_Cli
from cont_var import DG_NAMES as dg_names,IP_ADDRESS as ip_address


for dg_name in dg_names:
    for i in xrange(1,6):
        iscsi_vd_name = dg_name + 'iscsi' + str(i)
        iscsi_sys_cli = Sys_Cli(dg_name,iscsi_vd_name,ip_address)
        iscsi_sys_cli.create_iscsi_lun()
        iscsi_sys_cli.iscsi_lun_add_permission()
