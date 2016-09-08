#!/usr/bin/python

from get_sys_info import GetSysInfo
import sys_cli

sys_info = GetSysInfo()

dg_list = sys_info.get_dg_list()
iscsi_lun_list = sys_info.get_iscsi_lun_list()
nas_lun_list = sys_info.get_nas_lun_list()

if nas_lun_list :
    for nas_lun in nas_lun_list:
        sys_cli.SysCli()




