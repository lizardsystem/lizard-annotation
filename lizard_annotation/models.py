# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
# from django.db import models

import logging
import datetime
from django.db import models

from django_mongokit import connection
from django_mongokit.document import DjangoDocument

class Annotation(DjangoDocument):

    structure = {
       'title': unicode,
       # 'status': unicode,
       # 'annotation_type': unicode,
       # 'user_creator': unicode,
       # 'user_midifier': unicode,
       # 'dt_creation': datetime.datetime,
       # 'dt_modification': datetime.datetime,
       # 'relation_objects': {'name': unicode,
       #                      'id': unicode},
     }

connection.register([Annotation])


class AnnotationCategory(DjangoDocument):
    structure = {
        'category': unicode,
        }

    required_fields = ['category']

connection.register([AnnotationCategory])


class AnnotationType(DjangoDocument):
    structure = {
        'type': unicode,
        }

    required_fields = ['type']

connection.register([AnnotationType])


class AnnotationStatus(DjangoDocument):
    structure = {
        'status': unicode,
        }

    required_fields = ['status']

connection.register([AnnotationStatus])
