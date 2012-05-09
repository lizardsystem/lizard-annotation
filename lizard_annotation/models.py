# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.contrib.gis.db import models

from lizard_security.manager import FilteredGeoManager
from lizard_security.models import DataSet
from lizard_measure.models import (
    WaterBody,
    Measure,
)
from lizard_area.models import Area
from lizard_workspace.models import (
    LayerWorkspace,
    LayerCollage,
)

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
        items = ((field,getattr(self, field)) for field in fieldnames)
        result = {}
        for k, v in items:
            if isinstance(v, models.Model):
                # Replace object by representation
                result.update({k: str(v)})
                if ref_urls:
                    result.update({k + '_url': v.get_absolute_url()})
            else:
                result.update({k: v})
        return result

    def get_property_list(self, properties=None):
        obj_dict = self.get_dict()
        print obj_dict
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


class Annotation(models.Model, GettersMixin):
    """
    Annotation.
    """

    class Meta:
        verbose_name = _('Annotation')
        verbose_name_plural = _('Annotations')
    
    # View whose data to store via lizard_history.
    HISTORY_DATA_VIEW = ('lizard_annotation.api.views.AnnotationFormView')

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

    geom = models.GeometryField(
        null=True,
        blank=True,
        srid=4326,
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
        # Dirty trick to enforce default type for annotations
        default=1,
        verbose_name=_('Annotation type'),
    )
    annotation_category = models.ForeignKey(
        AnnotationCategory,
        null=True,
        blank=True,
        verbose_name=_('Annotation category'),
    )

    # Many-to-manies
    areas = models.ManyToManyField(
        Area,
        blank=True,
        related_name='annotation_set',
        verbose_name=_('Areas'),
    )
    waterbodies = models.ManyToManyField(
        WaterBody,
        blank=True,
        related_name='annotation_set',
        verbose_name=_('Waterbodies'),
    )
    measures = models.ManyToManyField(
        Measure,
        blank=True,
        related_name='annotation_set',
        verbose_name=_('Measures'),
    )
    workspaces = models.ManyToManyField(
        LayerWorkspace,
        blank=True,
        related_name='annotation_set',
        verbose_name=_('Workspaces'),
    )
    collages = models.ManyToManyField(
        LayerCollage,
        blank=True,
        related_name='annotation_set',
        verbose_name=_('Collages'),
    )

    # Cleared object tracking
    valid = models.BooleanField(
        default=True,
        verbose_name=_('Valid'),
    )

    # Security
    data_set = models.ForeignKey(DataSet,
                                 null=True,
                                 blank=True)

    objects = FilteredGeoManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_annotation',
            kwargs={'pk': self.pk},
        )

    def get_geometry_wkt_string(self):
        """
        Returns geometry in the well known text format
        """
        if self.geom is None:
            return ''
        else:
            return self.geom.wkt
