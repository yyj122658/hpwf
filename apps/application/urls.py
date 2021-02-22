# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 9:34
# @Author  : youngleesin
# @FileName: urls.py.py
# @Software: PyCharm

from django.conf.urls import url
import apps.application.views.ApplicationController_views as ApplicationAdmin

urlpatterns = [
    url(r'^Index/', ApplicationAdmin.Index),
    url(r'^IndexManage/', ApplicationAdmin.IndexManage),
]