#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import os
#
# def getfilename(filepath):
#     for root,dirs,files in os.walk(filepath):
#
#         for filename in files:
#             yield filename
#
#
#
# path = "H:\\"
#
# # getfilename(path)
# for file in getfilename(path):
#     print(file)

def count(n):
  for i in range(4):
    print("cunting: "+str(i))
    yield n  #生成值：n
    n -= 1

a=count(5)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())