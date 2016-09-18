#!/usr/bin/python
# -*- coding:utf-8 -*-

from sys_cli import SysCli
from cont_var import DG_NAMES_NAS as dg_names_nas,IP_ADDRESS as ip_address


for dg_name in dg_names_nas:
    for i in xrange(1,2):
        nas_vd_name = dg_name + 'nas' + str(i)
        nas_sys_cli = SysCli(dg_name,nas_vd_name,ip_address)
        nas_sys_cli.create_nas_lun()
