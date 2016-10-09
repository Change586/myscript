#!/usr/bin/python
#--*-- encoding:utf-8 --*--
from read_sheet import get_data
from collections import Counter

def jiebao_data():

    path = r'D:\processed_data.xls'
    read_table_index = 1
    processed_col = 24

    data = get_data()

    table_data = data.get_table_data(path,read_table_index)
    col_values = data.get_col_values(table_data,processed_col-1)

    rows=table_data.nrows

    for row_num in xrange(1,rows):
        row_values = data.get_row_values(table_data,row_num)
        invoice_num = row_values[3]
        repertory_cell_value = data.extract_col_value(row_values[processed_col-1],'CNCS',8)
        sys_invoice_num = data.shifting_extract_col_value(row_values[processed_col-1],'发票号',4,12)
        extract_col_value = data.shifting_extract_col_value(col_value,'到期日',14)



    for col_value in col_values:
        extract_col_value = data.shifting_extract_col_value(col_value,'到期日',14)
        print extract_col_value