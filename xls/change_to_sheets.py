#!/usr/bin/python
#--*-- encoding:utf-8 --*--
__author__ = 'Change'

import xlwt
import sys

from read_sheet import get_process_data

new_xls = xlwt.Workbook()
sanfang_sheet = new_xls.add_sheet(r'sanfang')
jiebao_sheet = new_xls.add_sheet(r'jiebao')
dongfeng_sheet = new_xls.add_sheet(r'dongfeng')

path = 'D:\data.xls'

get_process_data = get_process_data()

table = get_process_data.get_table_data(path,0)

count_rows = table.nrows
count_cols = table.ncols

#col_values_list = get_process_data.get_col_values(table,23)

jiebao_row = 1
dongfeng_row = 1

for col in xrange(count_cols):
    jiebao_sheet.write(0,col,table.row_values(0)[col])
    dongfeng_sheet.write(0,col,table.row_values(0)[col])

for row in xrange(count_rows):
    row_values = get_process_data.get_row_values(table,row)
    if row_values[7] == '捷豹路虎汽车贸易（上海）有限公司' and row_values[20] == '否':
        for col in xrange(count_cols):
            jiebao_sheet.write(jiebao_row,col,row_values[col])
        jiebao_row = jiebao_row + 1
    elif row_values[7] == '东风本田发动机有限公司' and row_values[20] == '否':
        for col in xrange(count_cols):
            dongfeng_sheet.write(dongfeng_row,col,row_values[col])
        dongfeng_row = dongfeng_row + 1
    elif row_values[20] == '否':
        for col in xrange(count_cols):
            if col != count_cols-1 and col == 3:
                sanfang_sheet.write(row,0,row_values[col])
            elif col == count_cols-1:
                invoice_cell_value = get_process_data.shifting_extract_col_value(row_values[col],'发票号',12)
                repertory_cell_value = get_process_data.extract_col_value(row_values[col],'CNCS',8)
                sanfang_sheet.write(row,1,invoice_cell_value)
                sanfang_sheet.write(row,2,repertory_cell_value)

new_xls.save(r'D:\test.xls')

# extract_from_col_value_list = get_process_data.extract_from_col_value_list(col_values_list,'发票号',12)
#
# get_process_data.extract_from_col_value()