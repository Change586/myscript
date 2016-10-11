#!/usr/bin/python
#--*-- encoding:utf-8 --*--

import xlrd
import xlwt
from collections import Counter
import os

def merge_process(process_table,write_table):
    #获取列表中所有相同元素的索引号
    def get_equ_elem_index(value,list):
        reapt_values_dic = {}
        reapt_values_dic[value]=[]
        for i in xrange(len(list)):
            if list[i] == value:
                reapt_values_dic[value].append(i)
        return reapt_values_dic

    table_nrows = process_table.nrows
    table_ncols = process_table.ncols

    extract_col_num = 2
    sys_invoice = process_table.col_values(extract_col_num)

    sys_invoice_count_dict = dict(Counter(sys_invoice))
    sys_invoice_reapt_dict = {}

    #生产存在重复值及重复次数的键值对，系统发票号：重复次数
    for key,value in sys_invoice_count_dict.items():
        if key != '' and value > 1:
            sys_invoice_reapt_dict[key]=value

    sys_invoice_reapt_list = sys_invoice_reapt_dict.keys()

    # 将未有重复的行写入新的文件中
    write_row_num = 0
    repertory_col_num = 1
    sys_invoice_col_num = 2
    invoice_col_num = 4

    for rownum in xrange(0,table_nrows):
        if process_table.row_values(rownum)[extract_col_num] != '' and process_table.row_values(rownum)[extract_col_num] not in sys_invoice_reapt_list:
            write_table.write(write_row_num,0,'15610')
            write_table.write(write_row_num,1,process_table.row_values(rownum)[repertory_col_num])
            write_table.write(write_row_num,2,process_table.row_values(rownum)[sys_invoice_col_num])
            write_table.write(write_row_num,3,'RI')
            write_table.write(write_row_num,4,process_table.row_values(rownum)[invoice_col_num])

            write_row_num = write_row_num + 1

    if sys_invoice_reapt_list:
        #获取所有存在系统发票号相同的号及所对应的索引值
        all_reapt_values_dict = {}
        for reapt_sys_invoice_num in sys_invoice_reapt_list:
            reapt_values_dict = get_equ_elem_index(reapt_sys_invoice_num,sys_invoice)
            all_reapt_values_dict = dict(all_reapt_values_dict,**reapt_values_dict)

        #合并处理相同系统发票号的行数据,并追加写入新xls文件中
        for key,values in all_reapt_values_dict.items():

            #获取系统发票号相同的数据中的发票号最小值的索引和最大值的索引，为后面合并发票号做准备
            invoice_num = []
            for value in values:
                invoice_num.append(process_table.row_values(value)[invoice_col_num])

            print invoice_num

            invoice_num = map(int,invoice_num)

            min_invoice_num = min(invoice_num)
            max_invoice_num = max(invoice_num)
            space = max_invoice_num - min_invoice_num

            if space <= 100:

                min_invoice_index = invoice_num.index(min_invoice_num)
                max_invoice_index = invoice_num.index(max_invoice_num)

        #        print min_invoice_index,max_invoice_index

                write_table.write(write_row_num,0,'15610')
                write_table.write(write_row_num,1,process_table.row_values(values[min_invoice_index])[repertory_col_num])
                write_table.write(write_row_num,2,process_table.row_values(values[min_invoice_index])[sys_invoice_col_num])
                write_table.write(write_row_num,3,'RI')
                write_table.write(write_row_num,4,process_table.row_values(values[min_invoice_index])[invoice_col_num] + '-' \
                                + process_table.row_values(values[max_invoice_index])[invoice_col_num][-5:])

                write_row_num = write_row_num + 1
            else:
                pass

    # file_name = r'D:\test.xls'
    # if os.path.exists(file_name):
    #     os.remove(file_name)





