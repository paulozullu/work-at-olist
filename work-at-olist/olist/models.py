# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    """
    Categories and subcategories. Uses adjacency model.
    """
    name = models.CharField(max_length=50,blank=True,null=False)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    channel_id = models.ForeignKey('Channel', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'category'
    
    def __unicode__(self):
        return self.name
    

class Channel(models.Model):
    """
    Channels.
    """
    name = models.CharField(max_length=50,blank=False,null=False)

    class Meta:
        db_table = 'channel'

    def __unicode__(self):
        return self.name

