# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Crocodile3'
__mtime__ = '2018/11/21'
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
import base64
import hashlib


class UserService():
    @staticmethod
    def genePwd(pwd,salt):
        m = hashlib.md5()
        str = "{}-{}".format(base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()