# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

import mongoengine
import copy

from django.core.urlresolvers import reverse


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


class AnnotationType(mongoengine.Document, GettersMixin):

    annotation_type = mongoengine.StringField()

    def __unicode__(self):
        return self.annotation_type

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_type', kwargs={'pk': self.pk})


class AnnotationCategory(mongoengine.Document, GettersMixin):

    category = mongoengine.StringField()
    annotation_type = mongoengine.ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.category

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_category',
            kwargs={'pk': self.pk},
        )


class AnnotationStatus(mongoengine.Document, GettersMixin):

    status = mongoengine.StringField()
    annotation_type = mongoengine.ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_status', kwargs={'pk': self.pk})


class Annotation(mongoengine.Document, GettersMixin):
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
