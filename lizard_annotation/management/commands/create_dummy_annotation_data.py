#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.core.management.base import BaseCommand

from lizard_annotation.mongodb_queries import insert_dummy_data

import logging
log = logging.getLogger("")


class Command(BaseCommand):
    """
    Create dummy annotation data.
    """

    def handle(self, *args, **options):

        insert_dummy_data()

