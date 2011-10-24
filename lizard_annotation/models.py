# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
# from django.db import models

import mongoengine

from django.core.urlresolvers import reverse


class ReferenceObject(mongoengine.EmbeddedDocument):

    reference_id = mongoengine.IntField()
    reference_model = mongoengine.StringField()
    reference_name = mongoengine.StringField()
    reference_filter = mongoengine.StringField()

    def __unicode__(self):
        return self.reference_filter


class AnnotationType(mongoengine.Document):

    annotation_type = mongoengine.StringField()

    def __unicode__(self):
        return self.annotation_type

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_type', kwargs={'pk': self.pk})


class AnnotationCategory(mongoengine.Document):

    category = mongoengine.StringField()
    annotation_type = mongoengine.ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.category

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_category',
            kwargs={'pk': self.pk},
        )


class AnnotationStatus(mongoengine.Document):

    status = mongoengine.StringField()
    annotation_type = mongoengine.ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_status', kwargs={'pk': self.pk})


class Annotation(mongoengine.Document):
    """
    reference_object field expects a dict. object
    like {"Gebied100": RelatedObject,}.
    """

    title = mongoengine.StringField()
    status = mongoengine.ReferenceField(AnnotationStatus)
    annotation_type = mongoengine.ReferenceField(AnnotationType)
    category = mongoengine.ReferenceField(AnnotationCategory)
    period_start = mongoengine.DateTimeField()
    period_end = mongoengine.DateTimeField()
    user_creator = mongoengine.StringField()
    user_modifier = mongoengine.StringField()
    dt_creation = mongoengine.DateTimeField()
    dt_modification = mongoengine.DateTimeField()
    reference_objects = mongoengine.DictField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_annotation',
            kwargs={'pk': self.pk},
        )
