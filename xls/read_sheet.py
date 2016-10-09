#!/usr/bin/python
#--*-- encoding:utf-8 --*--
__author__ = 'Change'

import xlrd
import sys
from collections import Counter



class get_data(object):
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

    #按偏移量从单元格中提取出想要的字段，并返回该字段
    def shifting_extract_col_value(self,col_value,target_string,shifting_num,extract_len=None):
        try:
            start_index = col_value.index(target_string)
            if extract_len:
                end_index = start_index + extract_len
            else:
                end_index = None
            extract_col_value = col_value[(start_index+shifting_num):end_index]
        except ValueError:
            extract_col_value = ""
        except:
            info = sys.exc_info()
            extract_col_value = info[1]

        return extract_col_value

    #从单元格中提取出想要的字段，并返回该字段
    def extract_col_value(self,col_value,target_string,extract_len):
        try:
            start_index = col_value.index(target_string)
            end_index = start_index + extract_len
            extract_col_value = col_value[start_index:end_index]
        except ValueError:
            extract_col_value = ""
        except:
            info = sys.exc_info()
            extract_col_value = info[1]

        return extract_col_value

    #获取某列中非空重复值与行号的对应dict
    def reapt_value_indexs_dict(self,table_data,processed_col):
        count_col_value_dict = dict(Counter(table_data.col_values(processed_col)))
        col_value_list = table_data.col_values(processed_col)

        reapt_values_dict = {}
        for key, value in count_col_value_dict.items():
            if key != '' and value > 1:
                reapt_values_dict[key] = value

        reapt_values_list = reapt_values_dict.keys()

        reapt_value_indexs_dict = {}
        for reapt_value in reapt_values_list:
            reapt_value_indexs_dict[reapt_value] = []
            if reapt_value != '':
                for index in xrange(len(col_value_list)):
                    if col_value_list[index] == reapt_value:
                        reapt_value_indexs_dict[reapt_value].append(index)
        return reapt_value_indexs_dict

    #获取某列中非空的唯一值列表
    def unique_values_list(self,table_data,processed_col):
        count_col_value_dict = dict(Counter(table_data.col_values(processed_col)))
        unique_values_list = []

        for key,value in count_col_value_dict.items():
            if key != '' and value == 1:
                unique_values_list.append(key)

        return unique_values_list












