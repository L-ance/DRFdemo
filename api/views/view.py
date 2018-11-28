#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/21

from rest_framework import filters
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from api import models
from api.serializers import basic
# from api.service import filters


class GenericsApiView(ListAPIView):

    queryset = models.Tag.objects.all()
    serializer_class = basic.TagSerializer

    # `SearchFilter`
    # filter_backends = (filters.SearchFilter, )
    # search_fields = ("tag_type", "name", )  # 多字段进行过滤

    # `Filter`
    # filter_backends = (filters.DjangoFilterBackend, )
    # filter_fields = ("tag_type", "order", )  # 指定字段过滤

    # 定制 `filter`
    # filter_backends = (filters.TagTypeFilter, )

    # 排序
    filter_backends = (filters.OrderingFilter, )
    ordering = ("-date", )  # 默认排序字段
    ordering_fields = ("date", )  # 可指定排序字段
    # 类推出自定义排序

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
