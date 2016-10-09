#!/usr/bin/python
#--*-- encoding:utf-8 --*--

from read_sheet import get_data
from collections import Counter

path = r'D:\processed_data.xls'
read_table_index = 1
processed_col = 24

data = get_data()

table_data = data.get_table_data(path,read_table_index)
col_values = data.get_col_values(table_data,processed_col-1)

for col_value in col_values:
    if col_value != '备注':
        sys_invoice_num = data.shifting_extract_col_value(col_value,'发票号',4,12)
        sys_invoice_len = len(sys_invoice_num)
        extract_col_value = data.shifting_extract_col_value(col_value,'到期日',14)
        sys_invoice_list = []

        if extract_col_value:
            sys_invoices_temp_list = extract_col_value.split('/')

            for sys_invoice in sys_invoices_temp_list:

                if '-' in sys_invoice:
                    leng = sys_invoice.index('-')
                else:
                    leng = len(sys_invoice)

                end_index = sys_invoice_len - leng
                if leng != sys_invoice_len:
                    sys_invoice = sys_invoice_num[:end_index]+sys_invoice
                    sys_invoice_list.append(sys_invoice)
                else:
                    sys_invoice_list.append(sys_invoice)

        else:
            sys_invoice_list.append(sys_invoice_num)

        print sys_invoice_list




