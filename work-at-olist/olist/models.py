# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    """
    Categories and subcategories. Uses adjacency model.
    """
    name = models.CharField(max_length=50,blank=True,null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    channel = models.ForeignKey('Channel', related_name='categories', on_delete=models.CASCADE, null=False, blank=False)

    def get_parent(self):
        return self.name + ' is subcategory of ' + self.parent.name + '.'

    def get_channel(self):
        return self.name + ' belongs to ' + self.channel.name + ' channel.'

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

