# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
# from django.db import models

import logging
import datetime

from mongoengine import StringField
from mongoengine import IntField
from mongoengine import DateTimeField
from mongoengine import ListField
from mongoengine import DictField
from mongoengine import ReferenceField
from mongoengine import EmbeddedDocument
from mongoengine import EmbeddedDocumentField
from mongoengine import Document


class ReferenceObject(EmbeddedDocument):

    reference_key = IntField()
    name = StringField()
    reference_filter = StringField()


class AnnotationStatus(Document):

    status = StringField()


class AnnotationCategory(Document):

    category = StringField()


class AnnotationType(Document):

    annotation_type = StringField()


class Annotation(Document):

    title = StringField()
    status =  ReferenceField(AnnotationStatus)
    annotation_type =  ReferenceField(AnnotationType)
    category = ReferenceField(AnnotationCategory)
    user_creator = EmbeddedDocumentField(ReferenceObject)
    user_modifier = EmbeddedDocumentField(ReferenceObject)
    dt_creation = DateTimeField()
    dt_modification = DateTimeField()
    reference_objects = ListField(ReferenceObject)

