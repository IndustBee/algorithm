# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:18:09 2018

@author: xiaojianren 
"""
#查看工作路径
import os
print(os.getcwd())

def ha():
    print('xiaojianren')

#在当前模块引用其它的模块， 将被引用模块加入搜索目录中   
import sys
sys.path.append('C:/Users/田茂松/.spyder-py3/temp.py')

import temp
print_max(1,2)


dir()

#不想直接换行之下的操作
print('a',end=' ')
print('b')

#创建一个空的tuple和只有一个元素的tuple
a=()
b=(1,)

#ASCII大小写字母数值为（65，90）和（97，122），用chr()转化成字母
def is_palindrome(s):
    if len(s)==0:
        print('not a string')
    else:
        ss=[]
        for i in s:
            if i in [chr(x) for x in range(65,91)] :
                ss.append(i)
            elif i in [chr(y) for y in range(97,123)]:
                ss.append(i)
            else:
                continue
    flag=0
    for j in range(len(ss)):
        if ss[j]!=ss[-1-j]:
            print('is not palindrome')
            flag=1
            break
    if flag==0:
        print('is palindrome')
    
            

