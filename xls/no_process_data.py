__author__ = 'Change'

#!/usr/bin/python
#--*-- encoding:utf-8 --*--
from read_sheet import get_data
from spread_sys_invoice import spread_sys_invoice
import xlwt

def no_process_data(row_values,new_table,write_row_num):
    new_table.write(write_row_num,1,row_values[3])
    new_table.write(write_row_num,2,row_values[7])
    new_table.write(write_row_num,3,row_values[20])
    new_table.write(write_row_num,4,row_values[23])
    write_row_num = write_row_num + 1

    return write_row_num