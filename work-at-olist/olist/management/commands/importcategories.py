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
    

    def import_categories(self, channel_name, filename):
        """
        Import categories to the database.

            Args:
                channel_name (str): The name of the channel that owns the categories.
                filename (str): Path to the file containing the categories to be imported.
        """
        
        channel, created = Channel.objects.get_or_create(name=channel_name)
        
        file = open(filename, 'r').readlines()
        
        for row in file:
            categories = row.split('//')
            depth = len(categories) - 1
            parent_id = None

            for x in range(0, depth):
                category, created = Category.objects.get_or_create(name=category[x].trim(), channel_id=result.id, parent_id=parent_id)
                parent_id = category.id


               


