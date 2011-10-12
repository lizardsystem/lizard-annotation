# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
# from django.db import models

import logging
import datetime

from mongoengine import StringField
from mongoengine import Document

class Annotation(Document):

    title = StringField()


# from django_mongokit import connection
# from django_mongokit.document import DjangoDocument


# @connection.register
# class Annotation(DjangoDocument):

#     __collection__ = 'annotations'
#     __database__ = 'vss'

#     structure = {
#         'title': unicode,
#         'status': unicode,
#         'annotation_type': unicode,
#         'user_creator': unicode,
#         'user_midifier': unicode,
#         'dt_creation': datetime.datetime,
#         'dt_modification': datetime.datetime,
#         'relation_objects': {unicode:[{'id': int, 'filter': unicode}}]
#     }

#     indexes = [
#        {'fields': ['relation_objects.$unicode']},
#      ]

#     use_dot_notation = True


# @connection.register
# class AnnotationCategory(DjangoDocument):

#     __collection__ = 'annotations_categories'
#     __database__ = 'vss'

#     structure = {
#         'category': unicode,
#         }

#     required_fields = ['category']

# connection.register([AnnotationCategory])


# @connection.register
# class AnnotationType(DjangoDocument):

#     __collection__ = 'annotation_type'
#     __database__ = 'vss'

#     structure = {
#         'type': unicode,
#         }

#     required_fields = ['type']


# @connection.register
# class AnnotationStatus(DjangoDocument):

#     __collection__ = 'annotation_statuses'
#     __database__ = 'vss'

#     structure = {
#         'status': unicode,
#         }

#     required_fields = ['status']

# def my_callback(sender, **kwargs):
#     print "Request finished!"

# # Code to put somewhere else
# # from django.db.models.signals import post_save
# # from django.dispatch import receiver
# #
# # @receiver(post_save)
# # def my_callback(sender, **kwargs):
# #     print "Saved!"
# #     print sender
# #     print kwargs

# # Annotation.find({'title':{'$regex':'^Yet'}}).next()
