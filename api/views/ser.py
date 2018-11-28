#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/21

from rest_framework import generics
from rest_framework.response import Response

from api import models
from api.serializers import custom


class DynamicFieldsApiView(generics.ListAPIView):

    queryset = models.Tag.objects.all()
    serializer_class = custom.DynamicTagSerializer

    fields = ("id", "name", )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True, fields=self.fields)
        return Response(serializer.data)


class CustomFieldsApiView(generics.ListAPIView):

    queryset = models.Article.objects.all()
    serializer_class = custom.CustomFieldSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
