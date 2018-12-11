# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os

# 路径配置;项目的路径
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
# 项目对应的文件夹路径，拼接存放测试用例的路径
CASE_PATH = os.path.join(BASE_PATH, 'Testcase')
Log_PATH= os.path.join(BASE_PATH, 'log')
path = r'D:\Workspace\BItestData\Testcase\api.xls'

