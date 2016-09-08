from sys_cli import SysCli
from cont_var import DG_NAMES as dg_names,IP_ADDRESS as ip_address


for dg_name in dg_names:
    for i in xrange(1,16):
        iscsi_vd_name = dg_name + 'iscsi' + str(i)
        iscsi_sys_cli = SysCli(dg_name,iscsi_vd_name,ip_address)
        iscsi_sys_cli.DelIscsiLun()

