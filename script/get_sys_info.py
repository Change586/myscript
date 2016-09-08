#!/usr/bin/python
import commands

class GetSysInfo(object):
    def __init__(self):
        pass

    def get_dg_list(self):
        dg_list = []
        dg_list_string = commands.getoutput('ucli dg_query_all')
        dg_list_temp = dg_list_string.split('\n')

        for dg in dg_list_temp:
            if dg.startswith('count')==False:
                dg_list.append(dg)

        return dg_list

    def get_iscsi_lun_list(self):
        iscsi_lun_list = []
        iscsi_lun_list_string = commands.getoutput('ucli vd_iscsi -l | awk \'{print $1,$2}\'')
        iscsi_lun_list_temp = iscsi_lun_list_string.split('\n')

        for iscsi_lun in iscsi_lun_list_temp:
            if iscsi_lun != 'vd_name' and iscsi_lun != '':
                iscsi_lun_list.append(iscsi_lun)

        return iscsi_lun_list

    def get_nas_lun_list(self):
        nas_lun_list = []
        nas_lun_list_string = commands.getoutput('ucli vd_nas -l | awk \'{print $2}\'')
        nas_lun_list_temp = nas_lun_list_string.split('\n')

        for nas_lun in nas_lun_list_temp:
            if nas_lun != 'vd_name' and nas_lun != '':
                nas_lun_list.append(nas_lun)

        return nas_lun_list



