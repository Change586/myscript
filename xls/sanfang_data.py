#!/usr/bin/python
#--*-- encoding:utf-8 --*--
__author__ = 'Change'

from read_sheet import get_data
from collections import Counter
import xlwt

def sanfang_data(row_values,sanfang_table,sanfang_write_row_num,no_process_table,no_process_write_row_num):
    processed_col = 24
    data = get_data()
    invoice_num = row_values[3]
    sys_invoice_string = row_values[processed_col-1]
    repertory_cell_value = '    ' + data.extract_col_value(sys_invoice_string,'CNCS',8)
    sys_invoice_num = data.shifting_extract_col_value(sys_invoice_string,'发票号',4,12)

    if sys_invoice_num:
        sanfang_table.write(sanfang_write_row_num,0,'15610')
        sanfang_table.write(sanfang_write_row_num,1,repertory_cell_value)
        sanfang_table.write(sanfang_write_row_num,2,sys_invoice_num)
        sanfang_table.write(sanfang_write_row_num,3,'RI')
        sanfang_table.write(sanfang_write_row_num,4,invoice_num)
        sanfang_write_row_num = sanfang_write_row_num + 1
    else:
        no_process_table.write(no_process_write_row_num,1,row_values[3])
        no_process_table.write(no_process_write_row_num,2,row_values[7])
        no_process_table.write(no_process_write_row_num,3,row_values[20])
        no_process_table.write(no_process_write_row_num,4,row_values[23])
        no_process_write_row_num = no_process_write_row_num + 1

        return no_process_write_row_num

    return sanfang_write_row_num


if __name__ == '__main__':
    pass