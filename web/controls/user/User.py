# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Crocodile3'
__mtime__ = '2018/11/16'
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

from flask import Blueprint
from flask import render_template

route_user = Blueprint('user_page',__name__)


@route_user.route("/login")
def login():
    return render_template('user/login.html')


@route_user.route("/edit")
def edit():
    return render_template("user/edit.html")
    
    
@route_user.route("/reset-pwd")
def resetPwd():
    return render_template("user/reset_pwd.html")