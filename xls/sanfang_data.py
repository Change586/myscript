#!/usr/bin/python
#--*-- encoding:utf-8 --*--
__author__ = 'Change'

from read_sheet import get_data
from collections import Counter
import xlwt

def sanfang_data(row_values,new_table,write_row_num):
    processed_col = 24
    data = get_data()
    invoice_num = row_values[3]
    sys_invoice_string = row_values[processed_col-1]
    repertory_cell_value = '    ' + data.extract_col_value(sys_invoice_string,'CNCS',8)
    sys_invoice_num = data.shifting_extract_col_value(sys_invoice_string,'发票号',4,12)

    if sys_invoice_num:
        new_table.write(write_row_num,0,'15610')
        new_table.write(write_row_num,1,repertory_cell_value)
        new_table.write(write_row_num,2,sys_invoice_num)
        new_table.write(write_row_num,3,'RI')
        new_table.write(write_row_num,4,invoice_num)
        write_row_num = write_row_num + 1

    return write_row_num


if __name__ == '__main__':
    pass