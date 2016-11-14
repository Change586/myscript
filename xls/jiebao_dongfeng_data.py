#!/usr/bin/python
#--*-- encoding:utf-8 --*--
from read_sheet import get_data
from spread_sys_invoice import spread_sys_invoice
import xlwt

def jiebao_dongfeng_data(row_values,jiebao_dongfeng_table,jiebao_dongfeng_write_row_num,no_process_table,no_process_row_num):
    processed_col = 24
    data = get_data()
    invoice_num = row_values[3]
    sys_invoice_string = row_values[processed_col-1]
    repertory_cell_value = '    ' + data.extract_col_value(sys_invoice_string,'CNCS',8)
    sys_invoice_num = data.shifting_extract_col_value(sys_invoice_string,'发票号',4,12)
    spread_sys_invoice_list = spread_sys_invoice(sys_invoice_string)

    #print spread_sys_invoice_list

    if sys_invoice_num:
        for sys_invoice in spread_sys_invoice_list:
            jiebao_dongfeng_table.write(jiebao_dongfeng_write_row_num,0,'15610')
            jiebao_dongfeng_table.write(jiebao_dongfeng_write_row_num,1,repertory_cell_value)
            jiebao_dongfeng_table.write(jiebao_dongfeng_write_row_num,2,sys_invoice)
            jiebao_dongfeng_table.write(jiebao_dongfeng_write_row_num,3,'RI')
            jiebao_dongfeng_table.write(jiebao_dongfeng_write_row_num,4,invoice_num)
            jiebao_dongfeng_write_row_num = jiebao_dongfeng_write_row_num + 1

    else:
        no_process_table.write(no_process_row_num,0,row_values[3])
        no_process_table.write(no_process_row_num,1,row_values[7])
        no_process_table.write(no_process_row_num,2,row_values[20])
        no_process_table.write(no_process_row_num,3,row_values[23])
        no_process_row_num = no_process_row_num + 1

    return jiebao_dongfeng_write_row_num,no_process_row_num

# new_xls.save(r'D:\jiebao.xls')

if __name__ == '__main__':
    path = r'D:\processed_data.xls'
    read_table_index = 1

    data = get_data()

    table_data = data.get_table_data(path,read_table_index)
    # col_values = data.get_col_values(table_data,processed_col-1)

    rows=table_data.nrows

    table_name = 'jiebao'
    new_xls = xlwt.Workbook()
    new_table = new_xls.add_sheet(table_name)

    write_row_num = 0
    for row_num in xrange(1,rows):
        row_values = data.get_row_values(table_data,row_num)
        write_row_num = jiebao_dongfeng_data(row_values,new_table,write_row_num)

    new_xls.save(r'D:\jiebao.xls')