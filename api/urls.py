#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/20

from django.conf.urls import url
from django.conf.urls import include

from api.views import (
    basic,
    view,
    ser,
    demo,
)

# Basic CURD
basic_urlpatterns = [
    url(r"^tags/$", basic.ListCreateApiView.as_view()),
    url(r"^tag/(?P<pk>[0-9]+)", basic.RetrieveUpdateDestroyApiView.as_view())
]

# 视图类属性
view_urlpatterns = [
    url(r"^$", view.GenericsApiView.as_view())
]

# 序列化属性
ser_urlpatterns = [
    url(r"^fields/$", ser.DynamicFieldsApiView.as_view()),
    url(r"^custom/$", ser.CustomFieldsApiView.as_view())
]


urlpatterns = [
    url(r'^basic/', include(basic_urlpatterns)),

    url(r'^view/', include(view_urlpatterns)),
    url(r'^ser/', include(ser_urlpatterns)),

    url(r'^tree/(?P<pk>\d+)/$', demo.TreeSerView.as_view())
]
