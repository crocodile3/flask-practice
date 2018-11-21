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

route_account = Blueprint('account_page',__name__)


@route_account.route("/index")
def login():
    return render_template('account/index.html')


@route_account.route("/info")
def edit():
    return render_template("account/info.html")
    
    
@route_account.route("/set")
def resetPwd():
    return render_template("account/set.html")