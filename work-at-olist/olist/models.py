# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    """
    Categories, channels and subcategories. Uses adjacency model.
    """
    name = models.CharField(max_length=50,blank=True,null=False)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.name

