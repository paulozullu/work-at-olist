# -*- coding: utf-8 -*-
from olist.models import Category, Channel
from rest_framework import serializers


class RecursiveField(serializers.HyperlinkedModelSerializer):
    def to_native(self, value):
        return self.parent.to_native(value)

    class Meta:
        model = Category
        fields = ('name','url')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Category model.
    """
    sub_categories = RecursiveField(many=True)
    class Meta:
        model = Category
        fields = ('name', 'parent', 'channel','sub_categories')
        depth = 2


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Channel model.
    """
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Channel
        fields = ('name', 'categories')

        