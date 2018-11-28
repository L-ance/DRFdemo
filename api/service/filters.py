#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/21

from rest_framework.filters import BaseFilterBackend


class TagTypeFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        tag_type = request.query_params.get("tag_type")

        return queryset.filter(tag_type=tag_type)
