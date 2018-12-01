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
from flask import request,jsonify,make_response,redirect
from flask import Blueprint
from flask import render_template
from flask import logging
from common.models.User import User
from common.libs.User.UserService import UserService
from application import app,db
import json
from common.libs.UrlManager import UrlManager



import pymysql
pymysql.install_as_MySQLdb()

route_user = Blueprint('user_page',__name__)


@route_user.route("/login",methods=['GET','POST'])
def login():
    # 返回值信息
    msg = {"code":200,"msg":"登录成功","data":""}
    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        # 第一步：获取请求值
        resq = request.values
        # 获取用户名
        login_name = resq.get('login_name')
        # 获取用户输入的密码
        login_pwd = resq.get('login_pwd')
        # 第二步：对参数的有效性进行判断
        
    # 用户名判断
    if login_name is None or len(login_name) < 1:
        msg['code'] = -1
        msg['msg'] = '登录失败,请输入正确的用户名或密码'
        return jsonify(msg)
    
    # 密码判断
    if login_pwd is None or len(login_pwd) < 1:
        msg['code'] = -1
        msg['msg'] = '登录失败，请输入正确的用户名或密码'
        return jsonify(msg)
    
    # 判断用户是否存在
    # 先从数据库中获取用户
    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        msg['code'] = -1
        msg['msg'] = '用户名不存在'
        return jsonify(msg)
    
    if user_info.login_pwd != UserService.genePwd(login_pwd,user_info.login_salt):
        msg['code'] = -1
        msg['msg'] = '登录失败，请输入正确的用户名或密码-2'
        return jsonify(msg)
    
    # 设置cookie，并返回给浏览器
    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 120)  # 保存120天
    return response

@route_user.route("/edit")
def edit():
    return render_template("user/edit.html")
    
    
@route_user.route("/reset-pwd")
def resetPwd():
    return render_template("user/reset_pwd.html")

@route_user.route("logout")
def logout():
    response = make_response(redirect(UrlManager.buildUrl("/user/login")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response