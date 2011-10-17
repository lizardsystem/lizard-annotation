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

AanAfvoerGebied = (
    u'GebiedA',
    u'GebiedB'
)


class ReferenceObject(EmbeddedDocument):

    reference_id = IntField()
    reference_model = StringField()
    reference_filter = StringField()


class AnnotationType(Document):

    annotation_type = StringField()

    def __unicode__(self):
        return self.annotation_type


class AnnotationCategory(Document):

    category = StringField()
    annotation_type =  ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.category


class AnnotationStatus(Document):

    status = StringField()
    annotaition_type = ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.status


class Annotation(Document):

    title = StringField()
    status =  ReferenceField(AnnotationStatus)
    annotation_type =  ReferenceField(AnnotationType)
    category = ReferenceField(AnnotationCategory)
    user_creator = StringField()
    user_modifier = StringField()
    dt_creation = DateTimeField()
    dt_modification = DateTimeField()
    reference_objects = ListField(EmbeddedDocumentField(ReferenceObject))

    def __unicode__(self):
        return self.title
