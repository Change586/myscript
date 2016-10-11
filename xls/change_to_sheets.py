#!/usr/bin/python
#--*-- encoding:utf-8 --*--
__author__ = 'Change'

import xlwt
import sys
from jiebao_dongfeng_data import jiebao_dongfeng_data
from sanfang_data import sanfang_data
from read_sheet import get_data

def change_to_sheets(path,sys_invoice_col,invoice_col):
    new_xls = xlwt.Workbook()
    sanfang_sheet = new_xls.add_sheet(r'sanfang')
    jiebao_sheet = new_xls.add_sheet(r'jiebao')
    dongfeng_sheet = new_xls.add_sheet(r'dongfeng')

    get_process_data = get_data()

    table = get_process_data.get_table_data(path,0)

    count_rows = table.nrows
    count_cols = table.ncols

    #col_values_list = get_process_data.get_col_values(table,23)

    jiebao_row = 0
    dongfeng_row = 0
    sanfang_row = 0

    # for col in xrange(count_cols):
    #     # jiebao_sheet.write(0,col,table.row_values(0)[col])
    #     dongfeng_sheet.write(0,col,table.row_values(0)[col])

    for row in xrange(count_rows):
        row_values = get_process_data.get_row_values(table,row)
        if row_values[7] == '捷豹路虎汽车贸易（上海）有限公司' and row_values[20] == '否':
            jiebao_row = jiebao_dongfeng_data(row_values,jiebao_sheet,jiebao_row)
            # for col in xrange(count_cols):
            #     jiebao_sheet.write(jiebao_row,col,row_values[col])
            # jiebao_row = jiebao_row + 1

        elif row_values[7] == '东风本田发动机有限公司' and row_values[20] == '否':
            dongfeng_row = jiebao_dongfeng_data(row_values,dongfeng_sheet,dongfeng_row)
            # for col in xrange(count_cols):
            #     dongfeng_sheet.write(dongfeng_row,col,row_values[col])
            # dongfeng_row = dongfeng_row + 1

        elif row_values[20] == '否':
            sanfang_row = sanfang_data(row_values,sanfang_sheet,sanfang_row)
            # for col in xrange(count_cols):
            #     if col != sys_invoice_col-1 and col == invoice_col-1:
            #         sanfang_sheet.write(row,0,row_values[col])
            #     elif col == count_cols-1:
            #         invoice_cell_value = get_process_data.shifting_extract_col_value(row_values[col],'发票号',4,12)
            #         repertory_cell_value = get_process_data.extract_col_value(row_values[col],'CNCS',8)
            #         sanfang_sheet.write(row,1,invoice_cell_value)
            #         sanfang_sheet.write(row,2,repertory_cell_value)

    new_xls.save(r'D:\test.xls')

if __name__=="__main__":
    path=r'D:\20160901-30.xls'
    sys_invoice_col = 24
    invoice_col = 4
    change_to_sheets(path,sys_invoice_col,invoice_col)