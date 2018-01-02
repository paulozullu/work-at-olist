from django.test import TestCase
from .models import Channel, Category


class ChannelTest(TestCase):
    """ Test module for Channel model """

    def setUp(self):
        Channel.objects.create(
            name='submarino')
        Channel.objects.create(
            name='amazon')


class CategoryTest(TestCase):
    """ Test module for Category model """
    def setUp(self):
        
        submarino_channel, submarino_created = Channel.objects.get_or_create(name='submarino')
        category, _ = Category.objects.get_or_create(
            name='Sports', parent=None, channel=submarino_channel)
        Category.objects.create(
            name='Surf', parent=category, channel=submarino_channel)
        
        amazon_channel, amazon_created = Channel.objects.get_or_create(name='amazon')
        category, _ = Category.objects.get_or_create(
            name='Sports', parent=None, channel=amazon_channel)
        Category.objects.create(
            name='Soccer', parent=category, channel=amazon_channel)
        
        
    def test_category_channel(self):
        submarino_channel = Channel.objects.get(name='submarino')
        category_surf = Category.objects.get(name='Surf', channel=submarino_channel)
        self.assertEqual(category_surf.get_channel(), "Surf belongs to submarino channel.")
        self.assertEqual(category_surf.get_parent(), "Surf is subcategory of Sports.")

        amazon_channel = Channel.objects.get(name='amazon')
        category_soccer = Category.objects.get(name='Soccer', channel=amazon_channel)
        self.assertEqual(category_soccer.get_channel(), "Soccer belongs to amazon channel.")
        self.assertEqual(category_soccer.get_parent(), "Soccer is subcategory of Sports.")

