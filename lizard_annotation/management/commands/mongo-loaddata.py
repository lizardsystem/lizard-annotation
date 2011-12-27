#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.core.management.base import BaseCommand
from django.conf import settings
from django_load import core as django_load

import pkg_resources
import mongoengine
import subprocess
import pprint
import sys
import os

# Command specifications for use in subprocess
MONGO_IMPORT_ARGS = [
    'mongoimport',
    '--db',
    settings.MONGODB_NAME,
    '--host',
    str(settings.MONGODB_SETTINGS.get('host')) + ':' +
    str(settings.MONGODB_SETTINGS.get('port')),
    '--username',
    settings.MONGODB_SETTINGS.get('username'),
    '--password',
    settings.MONGODB_SETTINGS.get('password'),
    '--collection',
    ]
   

class Command(BaseCommand):
    """
    Import mongo data
    """

    def handle(self, *args, **options):
        """
        Mongoexport collections for corresponding to args.
        """
        if not args:
            sys.stderr.write('oops, need args\n')
            return
        import_process = None
        for file_name in args:
            mongo_file = open(file_name, 'r')
            for line in mongo_file:

                if not line.startswith('{'):
                    if import_process:
                        import_process.stdin.close()
                    collection = line.split()[0]

                    import_process = subprocess.Popen(
                        MONGO_IMPORT_ARGS + [collection],
                        stdin=subprocess.PIPE,
                    )
                    continue  # This header line should not go into mongoimport
                
                import_process.stdin.write(line)
        if import_process:
            import_process.stdin.close()
            import_process.wait()



