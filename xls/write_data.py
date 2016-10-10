#!/usr/bin/python
#--*-- encoding:utf-8 --*--
__author__ = 'Change'

import xlwt
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class write_process_data(object):
    def __init__(self):
        pass

    def write_data(self,file_path_name,table_name,row,col,data):
        new_xls = xlwt.Workbook()
        new_table = new_xls.add_sheet(table_name)
        new_table.write(row,col,data)
        new_xls.save(file_path_name)




