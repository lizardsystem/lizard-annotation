# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

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
    description = mongoengine.StringField()
    datetime_period_start = mongoengine.DateTimeField()
    datetime_period_end = mongoengine.DateTimeField()
    # References
    status = mongoengine.ReferenceField(AnnotationStatus)
    annotation_type = mongoengine.ReferenceField(AnnotationType)
    category = mongoengine.ReferenceField(AnnotationCategory)
    reference_objects = mongoengine.DictField()
    # Journaling
    datetime_created = mongoengine.DateTimeField()
    created_by = mongoengine.StringField()
    datetime_modified = mongoengine.DateTimeField()
    modified_by = mongoengine.StringField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_annotation',
            kwargs={'pk': self.pk},
        )
