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

# Load all models.py from all installed apps. Can be more selective.
django_load.load('models')
DOCS_DEFINED = mongoengine.Document.__subclasses__()
# Command specifications for use in subprocess

MONGO_EXPORT_ARGS = [
    'mongoexport',
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

FILTER_ARGS = [
    'python',
    pkg_resources.resource_filename(
        'lizard_annotation',
        'utils/filter.py',
    ),
    '--export',
]

def _export_with_header(collection):
    """
    Export data from collection to stdout with specific header
    """
    # sys.stderr.write("Exporting collection %s\n" % collection)

    export_process = subprocess.Popen(
        MONGO_EXPORT_ARGS + [collection],
        stdout=subprocess.PIPE,
        stderr=open(os.devnull, "w"),
    )

    filter_process = subprocess.Popen(
        FILTER_ARGS + [collection],
        stdin=export_process.stdout,
    )

    # Allow export_process to receive a SIGPIPE if filter_process exits;
    # See python docs for subprocess
    export_process.stdout.close()  


def _get_collection_names(arg):
    """
    Return collection name(s) of mongoengine documents for arg

    It is wrongly assumed that the mongoengine documents have been defined. Arg
    can be 'my_app' or 'my_app.my_document'.
    """

    try:
        app, doc = arg.split('.')
    except ValueError:
        app, doc = arg, None

    def _filter(klass):
        """
        Return if klass corresponds to app.doc
        """
        in_app = klass.__module__.split('.')[0] == app
        exact_doc = klass.__name__ == doc
        return in_app and (exact_doc or not doc)
    
    docs_selected = filter(
        _filter,
        DOCS_DEFINED,
    )

    collections = [document._meta['collection']
                   for document in docs_selected]
    return collections

    
class Command(BaseCommand):
    """
    Export mongo data
    """

    def handle(self, *args, **options):
        """
        Mongoexport collections for corresponding to args.
        """

        if not args:
            sys.stderr.write('oops, need args\n')
            return

        collections = set([])
        for arg in args:
            collections.update(_get_collection_names(arg))
        for collection in collections:
            _export_with_header(collection)
