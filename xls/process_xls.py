#!/usr/bin/python
#--*-- encoding:utf-8 --*--

import xlrd
import xlwt
from collections import Counter
import os

def process_xls():
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
    jiebao_table = workbook.sheets()[1]
    dongfeng_table = workbook.sheets()[2]

    jiebao_nrows = jiebao_table.nrows
    jiebao_ncols = jiebao_table.ncols

    dongfeng_nrows = dongfeng_table.nrows
    dongfeng_ncols = dongfeng_table.ncols

    nrows = table.nrows
    ncols = table.ncols

    extract_col_num = 1


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
    new_jiebao_table = new_file.add_sheet('jiebao')
    new_dongfeng_table = new_file.add_sheet('dongfeng')

    #复制sheet2中内容
    for row in xrange(jiebao_nrows):
        for col in xrange(jiebao_ncols):
            new_jiebao_table.write(row,col,jiebao_table.row_values(row)[col])

    #复制sheet3中内容
    for row in xrange(dongfeng_nrows):
        for col in xrange(dongfeng_ncols):
            new_dongfeng_table.write(row, col, dongfeng_table.row_values(row)[col])


    # 将未有重复的行写入新的文件中
    reapt_count = 0
    for rownum in xrange(0,nrows):
        if table.row_values(rownum)[extract_col_num] != '' and table.row_values(rownum)[extract_col_num] not in sys_invoice_reapt_list:
            new_table.write(rownum-reapt_count,0,'15610')
            new_table.write(rownum-reapt_count,1,table.row_values(rownum)[2])
            new_table.write(rownum-reapt_count,2,table.row_values(rownum)[1])
            new_table.write(rownum-reapt_count,3,'RI')
            new_table.write(rownum-reapt_count,4,table.row_values(rownum)[0])
        else:
            reapt_count = reapt_count+1

    #未重复数据的行数
    count_unique_rows = nrows - sum(sys_invoice_reapt_dict.values()) - sys_invoice_count_dict['']

    #获取所有存在系统发票号相同的号及所对应的索引值
    all_reapt_values_dict_list = []
    for reapt_sys_invoice_num in sys_invoice_reapt_list:
        reapt_values_dict = get_equ_elem_index(reapt_sys_invoice_num,sys_invoice)
        all_reapt_values_dict_list.append(reapt_values_dict)

    #合并处理相同系统发票号的行数据
    for reapt_value in all_reapt_values_dict_list:
        new_table.write(count_unique_rows,0,'15610')
        new_table.write(count_unique_rows,3,'RI')
        for keys,values in reapt_value.items():
            #获取系统发票号相同的数据中的发票号最小值的索引和最大值的索引，为后面合并发票号做准备
            invoice_num = []
            for value in values:
                invoice_num.append(table.row_values(value)[0])

            min_invoice_num = min(invoice_num)
            max_invoice_num = max(invoice_num)

            min_invoice_index = invoice_num.index(min_invoice_num)
            max_invoice_index = invoice_num.index(max_invoice_num)

    #        print min_invoice_index,max_invoice_index

            #处理系统发票号相同的数据，并追加写入新xls文件中
            for colnum in xrange(0, ncols):
                if colnum == 0:
                    new_table.write(count_unique_rows,4,table.row_values(values[min_invoice_index])[colnum] + '-' + table.row_values(values[max_invoice_index])[colnum][-2:])
                elif colnum == 1:
                    new_table.write(count_unique_rows,2,table.row_values(values[min_invoice_index])[colnum])
                elif colnum == 2:
                    new_table.write(count_unique_rows,1,table.row_values(values[min_invoice_index])[colnum])

            count_unique_rows = count_unique_rows + 1


    new_file.save(r'D:\processed_data.xls')

    file_name = r'D:\test.xls'
    if os.path.exists(file_name):
        os.remove(file_name)




