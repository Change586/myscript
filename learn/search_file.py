#-*-encoding:utf-8-*-

import os

def search_file(file_name,search_path='.'):
    file_name = []
    # if search_path == '.':
    #     dir_list = [dir_name for dir_name in os.listdir(search_path) if os.path.isdir(dir_name)]
    #     file_list = [dir_name for dir_name in os.listdir(search_path) if os.path.isfile(dir_name)]
    # else:
    #     dir_list = [dir_name for dir_name in os.listdir(search_path) if os.path.isdir(os.path.join(search_path)+dir_name)]
    #     file_list = [dir_name for dir_name in os.listdir(search_path) if os.path.isfile(os.path.join(search_path)+dir_name)]
    # #print dir_list
    #
if __name__=='__main__':
    search_file('test','E:\Program Files')

