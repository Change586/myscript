#!/usr/bin/python
#--*-- encoding:utf-8 --*--

from read_sheet import get_data
from collections import Counter

def spread_sys_invoice(col_value):
    data = get_data()
    sys_invoice_num = data.shifting_extract_col_value(col_value,'发票号',4,12)
    sys_invoice_len = len(sys_invoice_num)

    if '结算批号' in col_value:
        extract_col_value = data.extract_col_setion_value(col_value,'到期日',13,'结算批号')
    else:
        extract_col_value = data.shifting_extract_col_value(col_value,'到期日',13)

    extract_col_value = extract_col_value.strip()
    sys_invoice_list = []

    if extract_col_value:
        sys_invoices_temp_list = extract_col_value.split('/')
        # print sys_invoices_temp_list

        last_sys_invoice = sys_invoice_num

        for sys_invoice in sys_invoices_temp_list:
            if '-' in sys_invoice:
                leng = sys_invoice.index('-')
                end_index = sys_invoice_len - leng
                len_sys_invoice =  len(sys_invoice)

                if leng != sys_invoice_len:
                    #处理 60364208-4233/4268-4337/49/57-69和60363381-83/3463-3477/3535-38/3587-3661/65-77/3752-61/64-69/86两种特殊情况
                    if leng == len_sys_invoice/2:
                        prefix = last_sys_invoice[:end_index]
                        last_sys_invoice = prefix + sys_invoice[leng+1:]
                        sys_invoice = prefix + sys_invoice[:leng+1] + last_sys_invoice
                        sys_invoice_list.append(sys_invoice)
                    else:
                        leng2 = len_sys_invoice-leng-1
                        prefix = last_sys_invoice[:end_index]
                        prefix2 = last_sys_invoice[:end_index]+sys_invoice[:leng-leng2]
                        last_sys_invoice = prefix2 + sys_invoice[leng+1:]
                        sys_invoice = prefix + sys_invoice[:leng+1] + last_sys_invoice
                        sys_invoice_list.append(sys_invoice)
                else: #60364208-4233/4268-4337/60363381-83
                    if leng == len_sys_invoice/2:
                        last_sys_invoice = sys_invoice[leng+1:]
                        sys_invoice = sys_invoice[:leng+1] + last_sys_invoice
                        sys_invoice_list.append(sys_invoice)
                    else:
                        leng2 = len_sys_invoice-leng-1
                        prefix = sys_invoice[:leng-leng2]
                        last_sys_invoice = prefix + sys_invoice[leng+1:]
                        sys_invoice = sys_invoice[:leng+1] + last_sys_invoice
                        sys_invoice_list.append(sys_invoice)
            else: #没有‘-’
                leng = len(sys_invoice)
                end_index = sys_invoice_len - leng

                if leng != sys_invoice_len:
                    prefix = last_sys_invoice[:end_index]
                    last_sys_invoice = prefix + sys_invoice
                    sys_invoice = last_sys_invoice
                    sys_invoice_list.append(sys_invoice)
                else:
                    last_sys_invoice = sys_invoice
                    sys_invoice_list.append(sys_invoice)
            # print up_leng,up_sys_invoice


    else:
        sys_invoice_list.append(sys_invoice_num)

    # print sys_invoice_list

    #展开所有的系统发票号
    spread_sys_invoice_list = []

    for sys_invoice in sys_invoice_list:
        if '-' in sys_invoice:
            start_end = sys_invoice.split('-')
            start_end = map(int,start_end)
            for i in xrange(start_end[0],start_end[1]+1):
                spread_sys_invoice_list.append(i)
        else:
            sys_invoice = int(sys_invoice)
            spread_sys_invoice_list.append(sys_invoice)

    return spread_sys_invoice_list

if __name__ == '__main__':
    path = r'D:\processed_data.xls'
    read_table_index = 1
    processed_col = 24
    data = get_data()
    table = data.get_table_data(path,read_table_index)
    rows = table.nrows
    for row_num in xrange(1,rows):
        row_values = data.get_row_values(table,row_num)
        sys_invoice_string = row_values[processed_col-1]
        spread_sys_invoice_list = spread_sys_invoice(sys_invoice_string)

        #print spread_sys_invoice_list





