# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Crocodile3'
__mtime__ = '2018/11/17'
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

route_finance = Blueprint('finance_page', __name__)



@route_finance.route("/index")
def index():
    return render_template("finance/index.html")


@route_finance.route("/pay-info")
def pay_info():
    return render_template("finance/pay_info.html")

@route_finance.route("/account")
def account():
    return render_template('finance/account.html')


