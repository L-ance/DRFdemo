#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/20

from rest_framework import generics
from rest_framework.response import Response

from api import models
from api.serializers import (
    basic,
)


class ListCreateApiView(generics.ListCreateAPIView):

    """
    list:

        序列化多条数据

    create:

        创建单条数据OR多条数据

    """

    queryset = models.Tag.objects.all()
    serializer_class = basic.TagSerializer
    filter_backends = ()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({})
        else:
            return Response(serializer.errors)


class RetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    """

    retrieve:
        序列化单条数据

    update:
        更新单条数据

    destroy:
        删除数据

    """

    queryset = models.Tag.objects.all()
    serializer_class = basic.TagSerializer
    filter_backends = ()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({})
        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({})
