# -*- coding:UTF-8 -*-

from sys import argv # 从sys的包中引入argv功能模块

script, filename = argv # 参数变量

txt = open(filename) # 变量txt，打开命令行输入的文件

print "Here's your file %r:" % filename # 打印一行信息，指出用户输入的文件名称
print txt.read() # 打开文件的内容

print "Type the filename again:" # 打印一行信息，提示用户再次输入文件
file_again = raw_input("> ") # 变量file_again,传递用户输入的内容

txt_again = open(file_again) # 变量txt_again,打开用户输入的文件

print txt_again.read() # 打开用户再吃输入的文件

txtclose = txt.close()
txt_again = txt_again.close()