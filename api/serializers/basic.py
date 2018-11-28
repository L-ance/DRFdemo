#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/20

from rest_framework import serializers

from api import models


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = "__all__"
