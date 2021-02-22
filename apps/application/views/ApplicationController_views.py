# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 9:32
# @Author  : youngleesin
# @FileName: ApplicationController_views.py
# @Software: PyCharm

from apps.hadmin.MvcAppUtilties.LoginAuthorize import LoginAuthorize
from django.http.response import HttpResponse
from django.template import loader
from apps.hadmin.MvcAppUtilties.CommonUtils import CommonUtils

def IndexManage(request):
    """
    前台管理主页
    """
    response = HttpResponse()
    tmp = loader.get_template('Application/IndexManage.html')  # 加载模板
    render_content = {}  # 将要渲染到模板的数据
    new_body = tmp.render(render_content)  # 渲染模板
    response.content = new_body  # 设置返回内容
    return response

def Index(request):
    """
    前台主页
    """
    response = HttpResponse()
    tmp = loader.get_template('Application/Index.html')  # 加载模板
    render_content = {}  # 将要渲染到模板的数据
    new_body = tmp.render(render_content)  # 渲染模板
    response.content = new_body  # 设置返回内容
    return response
