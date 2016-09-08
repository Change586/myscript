#!/usr/bin/python
#--*-- encoding:utf-8 --*--

import xlrd
import xlwt
from collections import Counter

#获取列表中所有相同元素的索引号
def get_equ_elem_index(value,list):
    reapt_values_dic = {}
    reapt_values_dic[value]=[]
    for i in xrange(len(list)):
        if list[i] == value:
            reapt_values_dic[value].append(i)
    return reapt_values_dic

#读取原始表中数据
workbook = xlrd.open_workbook(r'D:\test.xls')
table = workbook.sheets()[0]
nrows = table.nrows
ncols = table.ncols

extract_col_num =16

sys_invoice = table.col_values(extract_col_num)
#sys_invoice_rem_reapt = list(set(sys_invoice))


sys_invoice_count_dict = dict(Counter(sys_invoice))
sys_invoice_reapt_dict = {}

#生产存在重复值及重复次数的键值对，系统发票号：重复次数
for key,value in sys_invoice_count_dict.items():
    if key != '' and value > 1:
        sys_invoice_reapt_dict[key]=value

sys_invoice_reapt_list = sys_invoice_reapt_dict.keys()

#创建新的待写入文件
new_file = xlwt.Workbook()
new_table = new_file.add_sheet('processed_data')

# 将未有重复的行写入新的文件中
reapt_count = 0
for rownum in xrange(0,nrows):
    if table.row_values(rownum)[extract_col_num] != '' and table.row_values(rownum)[extract_col_num] not in sys_invoice_reapt_list:
        for colnum in xrange(0,ncols):
            new_table.write(rownum-reapt_count,colnum,table.row_values(rownum)[colnum])
    else:
        reapt_count = reapt_count+1

#未重复数据的行数
count_unique_rows = nrows - sum(sys_invoice_reapt_dict.values()) - sys_invoice_count_dict['']

#获取所有存在系统发票号相同的号及所对应的索引值
all_reapt_values_dict_list = []
for reapt_sys_invoice_num in sys_invoice_reapt_list:
    reapt_values_dict = get_equ_elem_index(reapt_sys_invoice_num,sys_invoice)
    all_reapt_values_dict_list.append(reapt_values_dict)

#print all_reapt_values_dict_list

#合并处理相同系统发票号的行数据
for reapt_value in all_reapt_values_dict_list:
    for keys,values in reapt_value.items():
        #获取系统发票号相同的数据中的发票号最小值的索引和最大值的索引，为后面合并发票号做准备
        invoice_num = []
        for value in values:
            invoice_num.append(table.row_values(value)[3])

        min_invoice_num = min(invoice_num)
        max_invoice_num = max(invoice_num)

        min_invoice_index = invoice_num.index(min_invoice_num)
        max_invoice_index = invoice_num.index(max_invoice_num)

#        print min_invoice_index,max_invoice_index

        #处理系统发票号相同的数据，并追加写入新xls文件中
        for colnum in xrange(0, ncols):
            if colnum != 3:
                new_table.write(count_unique_rows,colnum,table.row_values(values[min_invoice_index])[colnum])
            else:
                new_table.write(count_unique_rows,colnum,table.row_values(values[min_invoice_index])[colnum] + '-' + table.row_values(values[max_invoice_index])[colnum][-2:])

        count_unique_rows = count_unique_rows + 1

new_file.save(r'D:\processed_data.xls')



