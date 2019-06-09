# -*- coding: utf-8 -*-#
"""
 FileName:     __init__.py
 Author:       jynnezhang
 Date:         2019/6/5
 Description:  
"""
# 引入 flask
from flask import Flask
# 导入 views 模块
from app import views

# 实例化一个flask 对象
app = Flask(__name__)
