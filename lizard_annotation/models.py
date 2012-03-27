# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models

import mongoengine
import copy

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

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
        fieldnames = (field.name for field in self._meta.fields)
        result = dict((field,getattr(self, field)) for field in fieldnames)
        if url:
            result.update(url=self.get_absolute_url())
        if ref_urls:
            result.update(dict(
                (key + '_url', value.get_absolute_url())
                for key, value in result.iteritems()
                if isinstance(value, models.Model)))
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


class AnnotationType(models.Model, GettersMixin):

    class Meta:
        verbose_name = _('Annotation type')
        verbose_name_plural = _('Annotation types')

    annotation_type = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Annotation type'),
    )

    def __unicode__(self):
        return self.annotation_type

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_type', kwargs={'pk': self.pk})


class AnnotationCategory(models.Model, GettersMixin):

    class Meta:
        verbose_name = _('Annotation category')
        verbose_name_plural = _('Annotation categories')

    annotation_category = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Annotation category'),
    )
    annotation_type = models.ForeignKey(
        AnnotationType,
        null=True,
        blank=True,
        verbose_name=_('Annotation type'),
    )

    def __unicode__(self):
        return self.annotation_category

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_category',
            kwargs={'pk': self.pk},
        )


class AnnotationStatus(models.Model, GettersMixin):

    class Meta:
        verbose_name = _('Annotation status')
        verbose_name_plural = _('Annotation statuses')

    annotation_status = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Annotation status'),
    )
    annotation_type = models.ForeignKey(
        AnnotationType,
        null=True,
        blank=True,
        verbose_name=_('Annotation type'),
    )

    def __unicode__(self):
        return self.annotation_status

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_status', kwargs={'pk': self.pk})


class ReferenceObject(models.Model, GettersMixin):
    """
    Object that refers to any possible object within the site. 
    """

    class Meta:
        verbose_name = _('Referred object')
        verbose_name_plural = _('Referred objects')

    annotation = models.ForeignKey('Annotation')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Annotation(models.Model, GettersMixin):

    class Meta:
        verbose_name = _('Annotation')
        verbose_name_plural = _('Annotations')
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
        verbose_name=_('Title'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )
    datetime_period_start = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('Date of start of period'),
    )
    datetime_period_end = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('Date of end of period'),
    )

    # References
    annotation_status = models.ForeignKey(
        AnnotationStatus,
        null=True,
        blank=True,
        verbose_name=_('Annotation status'),
    )
    annotation_type = models.ForeignKey(
        AnnotationType,
        null=True,
        blank=True,
        verbose_name=_('Annotation type'),
    )
    annotation_category = models.ForeignKey(
        AnnotationCategory,
        null=True,
        blank=True,
        verbose_name=_('Annotation category'),
    )
    reference_objects = models.ManyToManyField(
        ContentType,
        through='ReferenceObject',
        verbose_name=_('Referred objects'),
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
