# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models

import mongoengine
import copy

from django.contrib.contenttype.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


class GettersMixin(object):
    """
    Provides a get_dict() method and a get_property_list() method
    """
    def get_dict(self, url=False, ref_urls=False):
        """
        Return the fields and their contents as a dict.

        If url=True, add own absolute url, if ref_urls=True, add urls for any
        referencefields present.
        """
        self_copy = copy.deepcopy(self)
        result = dict([(key, self_copy[key]) for key in self_copy])
        if url:
            result.update(url=self_copy.get_absolute_url)
        if ref_urls:
            result.update([
                (key + '_url', self_copy[key].get_absolute_url())
                for key in self_copy
                if isinstance(self_copy[key], mongoengine.Document)])
        reference_objects = result.get('reference_objects')
        if reference_objects:
            for k in reference_objects:
                reference_objects[k] = reference_objects[k].get_dict()
        return result

    def get_property_list(self, properties=None):
        obj_dict = self.get_dict()
        if properties is None:
            properties = obj_dict.keys()
        property_list = []
        for p in properties:
            property_list.append({
                'property': p,
                'value': obj_dict[p],
            })
        return property_list


class ReferenceObject(mongoengine.EmbeddedDocument, GettersMixin):

    reference_id = mongoengine.StringField()
    reference_model = mongoengine.StringField()
    reference_name = mongoengine.StringField()
    reference_filter = mongoengine.StringField()

    def __unicode__(self):
        return self.reference_filter

# Here starts the postgres implementation...
class AnnotationType(models.Model, GettersMixin):

    annotation_type = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return self.annotation_type

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_type', kwargs={'pk': self.pk})


class AnnotationCategory(models.Model, GettersMixin):

    annotation_category = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    annotation_type = models.ForeignKey(
        AnnotationType,
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return self.category

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_category',
            kwargs={'pk': self.pk},
        )


class AnnotationStatus(models.Model, GettersMixin):

    annotation_status = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    annotation_type = models.ForeignKey(
        AnnotationType,
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_status', kwargs={'pk': self.pk})


class ReferenceObject(models.Model):
    annotation = models.ForeignKey('Annotation')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Annotation(models.Model):
    """
    Annotation.
    """
    """
    reference_object field expects a dict. object
    like {"Gebied100": RelatedObject,}.
    """
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    datetime_period_start = models.DateTimeField(
        null=True,
        blank=True,
    )
    datetime_period_end = models.DateTimeField(
        null=True,
        blank=True,
    )

    # References
    annotation_status = models.ForeignKey(
        AnnotationStatus,
        null=True,
        blank=True
    )
    annotation_type = models.ForeignKey(
        AnnotationType,
        null=True,
        blank=True
    )
    annotation_category = models.ForeignKey(
        AnnotationCategory,
        null=True,
        blank=True
    )
    reference_objects = models.ManyToMany(
        ContentType,
        through='ReferenceObject'
    )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #TODO
        """
        
        """
        return reverse(
            'lizard_annotation_api_annotation',
            kwargs={'pk': self.pk},
        )
