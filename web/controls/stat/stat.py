# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Crocodile3'
__mtime__ = '2018/11/18'
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

route_stat = Blueprint('stat_page', __name__)



@route_stat.route("/index")
def index():
    return render_template("stat/index.html")


@route_stat.route("/food")
def food():
    return render_template("stat/food.html")

@route_stat.route("/member")
def member():
    return render_template('stat/member.html')

@route_stat.route("/share")
def share():
    return render_template('stat/share.html')
