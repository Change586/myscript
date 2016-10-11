#!/usr/bin/python
#--*-- encoding:utf-8 --*--

import xlrd
import xlwt
from collections import Counter
import os
from merge_process import merge_process

def process_xls():
    #读取原始表中数据
    workbook = xlrd.open_workbook(r'D:\test.xls')
    sanfang_table = workbook.sheets()[0]
    jiebao_table = workbook.sheets()[1]
    dongfeng_table = workbook.sheets()[2]

    jiebao_nrows = jiebao_table.nrows
    jiebao_ncols = jiebao_table.ncols

    dongfeng_nrows = dongfeng_table.nrows
    dongfeng_ncols = dongfeng_table.ncols

    sanfang_nrows = sanfang_table.nrows
    sanfang_ncols = sanfang_table.ncols

    #创建新的待写入文件
    new_file = xlwt.Workbook()
    new_sanfang_table = new_file.add_sheet('sanfang_data')
    new_jiebao_table = new_file.add_sheet('jiebao')
    new_dongfeng_table = new_file.add_sheet('dongfeng')

    merge_process(sanfang_table,new_sanfang_table)
    merge_process(jiebao_table,new_jiebao_table)
    merge_process(dongfeng_table,new_dongfeng_table)

    new_file.save(r'D:\process_data.xls')

    # file_name = r'D:\test.xls'
    # if os.path.exists(file_name):
    #     os.remove(file_name)

if __name__ == '__main__':

    process_xls()



