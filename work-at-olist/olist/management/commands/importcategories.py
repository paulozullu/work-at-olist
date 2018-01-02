# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from olist.models import Category, Channel

class Command(BaseCommand):
    help = "Imports categories"

    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs='+', type=str)


    def handle(self, *args, **options):
        if len(options['arguments']) == 2:
            channel_name = options['arguments'][0]
            filename = options['arguments'][1]
            self.import_categories(channel_name, filename)
    

    def import_categories(self, channel_name, filename):
        """
        Import categories to the database.

            Args:
                channel_name (str): The name of the channel that owns the categories.
                filename (str): Path to the file containing the categories to be imported.
        """
        
        channel, _ = Channel.objects.get_or_create(name=channel_name)
        
        file = open(filename, 'r').readlines()
        
        for row in file:
            categories = row.strip().split('/')
            parent = None

            for category in categories:
                category_obj, created = Category.objects.get_or_create(name=category.strip(), channel=channel, parent=parent)
                parent = category_obj
        
