# -*- coding: utf-8 -*-
from workatolist.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Category model.
    """

    class Meta:
        model = Category
        fields = ('name', 'parent_id')

