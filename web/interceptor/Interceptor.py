# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Crocodile3'
__mtime__ = '2018/12/1'
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
from application import app
from flask import request,redirect
from common.models.User import User
from common.libs.User.UserService import UserService
from common.libs.UrlManager import UrlManager
import re


@app.before_request
def before_request():
    # 过滤掉不需要验证的url
    ignore_urls = app.config["IGNORE_URLS"]
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    
    path = request.path
    
    pattern = re.compile(r'%s'%"|".join(ignore_check_login_urls))
    
    if pattern.match(path):
        return
    
    user_info = check_login()

    pattern = re.compile(r'%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return
    
    
    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))
    
    return
    
def check_login():
    """
    判断用户是否已经登录
    :return:
    """
    cookies = request.cookies
    auth_cookie = cookies[app.config["AUTH_COOKIE_NAME"]] if app.config["AUTH_COOKIE_NAME"] in cookies else None
    app.logger.info(auth_cookie)
    # cookie的验证
    if auth_cookie is None:
        return False
    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False
    
    #从数据库中查询用户信息
    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception:
        return False
    
    if user_info is None:
        return False
    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False
    return user_info
    
    