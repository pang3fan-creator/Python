"""
项目目录
   主模块
   包(文件夹)
     模块(文件)
       类
         函数
           语句(今天又是充满希望的一天~)

请自己打造这样的项目结构， 执行函数
"""
# 项目的根目录开始
import myProject.pages.module as m
m.Stu().say()

from myProject.pages.module import *
Stu().say()