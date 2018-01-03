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
        
        channel, channel_created = Channel.objects.get_or_create(name=channel_name)
        
        if channel_created:
            print("Channel {0} created.".format(channel_name))
        else:
            print("Channel {0} updated.".format(channel_name))

        file = open(filename, 'r').readlines()
        
        for row in file:
            categories = row.strip().split('/')
            parent = None

            for category in categories:
                category_obj, category_created = Category.objects.get_or_create(name=category.strip(), channel=channel, parent=parent)

                if category_created:
                    if parent is None:
                        print("Category {0} created.".format(category.strip()))
                    else: 
                        print("Category {0}->{1} created.".format(parent.name, category.strip()))
                else:
                    if parent is None:
                        print("Category {0} updated.".format(category.strip()))
                    else: print("Category {0}->{1} updated.".format(parent.name, category.strip()))

                parent = category_obj
        
