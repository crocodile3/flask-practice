# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Crocodile3'
__mtime__ = '2018/11/15'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
DEBUG = True
SQLALCHEMY_ECHO = True  #将所有的SQL语句打印出来
SQLALCHEMY_DATABASE_URI = 'mysql://root:cyh187977@127.0.0.1/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = 'utf-8'
SERVER_PORT = 8999
AUTH_COOKIE_NAME = "mooc_food"


####过滤url####
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS =[
    "^/static",
    "/favicon.ico"
]