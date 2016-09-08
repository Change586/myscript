#!/usr/bin/python
#--*-- encoding:utf-8 --*--
__author__ = 'Change'

import xlrd
import sys
from collections import Counter



class get_process_data(object):
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

    #读取整张表数据
    def get_table_data(self,file_path,table_index):
        workbook = xlrd.open_workbook(file_path)
        table = workbook.sheets()[table_index]
        return table

    #获取某列数据
    def get_col_values(self,table,col_num):
        return table.col_values(col_num)

    #获取某行数据
    def get_row_values(self,table,row_num):
        return table.row_values(row_num)

    #获取某列中存在重复的数据及其重复的次数
    def get_col_value_reapt_dict(self,table,col_num):
        count_each_value_num_dict = dict(Counter(table.col_values(col_num)))
        reapt_value_num_dict = {}
        for key,value in count_each_value_num_dict:
            if key != '' and value > 1:
                reapt_value_num_dict[key] = value

        return reapt_value_num_dict

    ##获取某个重复值所对应的所有行号 {'value':[123,456...]}
    def get_value_index_dict(self,reapt_value,table_col_value_list):
        reapt_value_index_dict = {}
        reapt_value_index_dict[reapt_value] = []
        for i in len(table_col_value_list):
            if table_col_value_list[i] == reapt_value:
                reapt_value_index_dict[reapt_value].append(i)

        return reapt_value_index_dict

    #获取某列中存在的所有有重复的值，以及其所对应的所有行号 {'value':[123,456...],...}
    def get_all_reapt_value_index_dict(self,reapt_value_list,table_col_value_list):
        all_reapt_value_index_dict = {}
        for reapt_value in reapt_value_list:
            all_reapt_value_index_dict[reapt_value] = []
            for i in len(table_col_value_list):
                if table_col_value_list[i] == reapt_value:
                    all_reapt_value_index_dict[reapt_value].append(i)

        return all_reapt_value_index_dict

    #提取某列所有单元格中某个字段数据，返回新的列
    def extract_from_col_value_list(self,col_value_list,target_string,extract_len):
        extract_col_value_list = []
        for col_value in col_value_list:
            try:
                start_index = col_value.index(target_string)
                end_index = start_index + extract_len
                extract_col_value = col_value[(start_index+4):end_index]
                extract_col_value_list.append(extract_col_value)
            except ValueError:
                extract_col_value_list.append("")
            except:
                info = sys.exc_info()
                extract_col_value_list.append(info[1])

        return extract_col_value_list

    #从单元格中提取出想要的字段，并返回该字段
    def extract_from_col_value(self,col_value,target_string,extract_len):
        try:
            start_index = col_value.index(target_string)
            end_index = start_index + extract_len
            extract_col_value = col_value[(start_index+4):end_index]
        except ValueError:
            extract_col_value = ""
        except:
            info = sys.exc_info()
            extract_col_value = info[1]

        return extract_col_value







