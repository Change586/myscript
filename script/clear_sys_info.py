#!/usr/bin/python

from get_sys_info import GetSysInfo
from sys_cli import Sys_Cli
import sys

sys_info = GetSysInfo()

dg_list = sys_info.get_dg_list()
dg_iscsi_lun_dict = sys_info.get_dg_iscsi_lun_dict()
dg_nas_lun_dict = sys_info.get_dg_nas_lun_dict()

# print dg_list
# print dg_iscsi_lun_dict
# print dg_nas_lun_dict

try:
    if dg_iscsi_lun_dict:
        for key,values in dg_iscsi_lun_dict.iteritems():
            for value in values:
                print key,value
                ucli = Sys_Cli(key,value)
                ucli.del_iscsi_lun()
except:
    info = sys.exc_info()
    print 'del iscsi lun erro: ', info

try:
    if dg_nas_lun_dict:
        for key,values in dg_nas_lun_dict.iteritems():
            for value in values:
                ucli = Sys_Cli(key,value)
                ucli.del_nas_lun()
except:
    info = sys.exc_info()
    print 'del nas lun erro: ',info

try:
    if dg_list:
        for dg in dg_list:
            ucli = Sys_Cli(dg)
            ucli.del_dg()
except:
    info = sys.exc_info()
    print 'del nas lun erro: ',info






