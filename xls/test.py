#!/usr/bin/python
#--*-- encoding:utf-8 --*--

from read_sheet import get_process_data
from collections import Counter

path = r'D:\test.xls'
read_table_index = 0
processed_col = 1

get_process_data = get_process_data()

table_data = get_process_data.get_table_data(path,read_table_index)

count_rows = table_data.nrows
count_cols = table_data.ncols

reapt_value_indexs_dict = get_process_data.reapt_value_indexs_dict(table_data,processed_col)

reapt_values_list =  reapt_value_indexs_dict.keys()

reapt_count = 0
for row_num in xrange(count_rows):
    if table_data.row_values(row_num)[processed_col] != '' and table.row_values(row_num)[processed_col] not in reapt_values_list:
        new_table.write(row_num-reapt_count,0,'15610')
        new_table.write(row_num-reapt_count,1,table.row_values(rownum)[2])
        new_table.write(row_num-reapt_count,2,table.row_values(rownum)[1])
        new_table.write(row_num-reapt_count,3,'RI')
        new_table.write(row_num-reapt_count,4,table.row_values(rownum)[0])
    else:
        reapt_count = reapt_count+1





