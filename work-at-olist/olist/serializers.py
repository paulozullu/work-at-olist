# -*- coding: utf-8 -*-
from olist.models import Category, Channel
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Category model.
    """

    class Meta:
        model = Category
        fields = ('name', 'parent', 'channel',)


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Channel model.
    """
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Channel
        fields = ('name', 'categories')

        