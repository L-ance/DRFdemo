#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/29


from rest_framework import serializers

from api import models


class TreeSerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField()

    class Meta:
        model = models.Comment
        fields = "__all__"

    def get_children(self, instance):
        return self.__class__(instance.comment_set.all(), many=True, context=self.context).data
