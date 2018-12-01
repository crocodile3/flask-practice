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
######拦截器配置#########
from web.interceptor.Interceptor import *

from web.controls.index import route_index
from web.controls.user.User import route_user
from application import app
from web.controls.user.static import route_static
from web.controls.account.account import route_account
from web.controls.finance.finance import route_finance
from web.controls.member.member import route_member
from web.controls.stat.stat import route_stat
from web.controls.food.food import route_food

app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_account,url_prefix='/account')
app.register_blueprint(route_finance,url_prefix='/finance')
app.register_blueprint(route_member,url_prefix='/member')
app.register_blueprint(route_stat,url_prefix='/stat')
app.register_blueprint(route_food,url_prefix='/food')