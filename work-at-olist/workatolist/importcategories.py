# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Imports categories"

    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs='+', type=str)

    def handle(self, *args, **options):
        if len(options['arguments']) == 2:
            channel = options['arguments'][0]
            file = options['arguments'][1]
    
    def import_categories(self, channel, file):
        with open(file, 'r') as input_file:

