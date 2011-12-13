#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.core.management.base import BaseCommand
from django.conf import settings

import logging
import subprocess

log = logging.getLogger("")


class Command(BaseCommand):
    """
    Dump mongo data
    """

    def handle(self, *args, **options):
        settings.MONGODB_NAME
        command = 
        mongoexport
        # --db 
        # --host hostname:port

        # see if any apps are in the args
        # get all models for the given app that caused a collection
        # dump the commands using system command.
        db = settings.MONGODB_SETTINGS.get(
        dump = subprocess.check_output('mongoexport')
        print dump

