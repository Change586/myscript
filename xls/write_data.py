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

    def create_new_table(self,table_name):
        new_xls = xlwt.Workbook()
        new_table = new_xls.add_sheet(table_name)


