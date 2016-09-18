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
        iscsi_lun_list_string = commands.getoutput('ucli vd_iscsi -l | awk \'{print $2}\'')
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

    def get_dg_iscsi_lun_dict(self):
        dg_list =  self.get_dg_list()
        dg_iscsi_lun_dict = {}
        for dg in dg_list:
            iscsi_lun_string = commands.getoutput('ucli vd_iscsi -l | grep -w ' + dg + ' | awk \'{print $2}\'')
            iscsi_lun_list_temp = iscsi_lun_string.split('\n')
            dg_iscsi_lun_dict[dg] = iscsi_lun_list_temp

        return dg_iscsi_lun_dict

    def get_dg_nas_lun_dict(self):
        dg_list =  self.get_dg_list()
        dg_nas_lun_dict = {}
        for dg in dg_list:
            nas_lun_string = commands.getoutput('ucli vd_nas -l | grep -w ' + dg + ' | awk \'{print $2}\'')
            nas_lun_list_temp = nas_lun_string.split('\n')
            dg_nas_lun_dict[dg] = nas_lun_list_temp

        return dg_nas_lun_dict


if __name__ == '__main__':
    sys_info = GetSysInfo()
    dg_list = sys_info.get_dg_list()
    lun_list = sys_info.get_iscsi_lun_list()
    nas_list = sys_info.get_nas_lun_list()

    print dg_list
    print lun_list
    print nas_list




