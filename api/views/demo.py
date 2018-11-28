#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/29

from rest_framework.response import Response
from rest_framework import generics

from api import models
from api.serializers import demo


class TreeSerView(generics.RetrieveAPIView):

    queryset = models.Comment.objects.all()
    serializer_class = demo.TreeSerializer

    def retrieve(self, request, *args, **kwargs):
        ins = self.get_object()
        ser = self.get_serializer(ins)
        return Response(ser.data)
