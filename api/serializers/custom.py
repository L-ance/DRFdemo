#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/21

from django.conf import settings

from rest_framework import serializers

from api import models
from api.service import fields as custom_fields


class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class DynamicTagSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.Tag
        fields = "__all__"


class CustomFieldSerializer(serializers.ModelSerializer):
    # 自定义图片字段
    img = custom_fields.ImgPathField(prefix=settings.CDN_PATH)

    class Meta:
        model = models.Article
        fields = "__all__"
