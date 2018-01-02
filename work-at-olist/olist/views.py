# -*- coding: utf-8 -*-
from olist.models import Category, Channel
from rest_framework import viewsets 
from olist.serializers import CategorySerializer, ChannelSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories and subcategories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('-name')
    serializer_class = CategorySerializer


class ChannelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows channels to be viewed or edited.
    """    
    queryset = Channel.objects.all().order_by('-name')
    serializer_class = ChannelSerializer

    