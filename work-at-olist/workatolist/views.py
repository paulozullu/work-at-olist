# -*- coding: utf-8 -*-
from workatolist.models import Category
from rest_framework import viewsets 
from workatolist.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows channels, categories and subcategories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('-name')
    serializer_class = CategorySerializer

