# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

import mongoengine

from django.core.urlresolvers import reverse


class GetDictMixin(object):
    """
    Provides a get_dict() method.
    """
    def get_dict(self, url=False, ref_urls=False):
        """
        Return the fields and their contents as a dict.

        If url=True, add own absolute url, if ref_urls=True, add urls for any
        referencefields present.
        """
        result = dict([(key, self[key]) for key in self])
        if url:
            result.update(url=self.get_absolute_url)
        if ref_urls:
            result.update([
                (key + '_url', self[key].get_absolute_url())
                for key in self
                if isinstance(self[key], mongoengine.Document)])
        reference_objects = result.get('reference_objects')
        if reference_objects:
            for k in reference_objects:
                reference_objects[k] = reference_objects[k].get_dict()
        return result


class ReferenceObject(mongoengine.EmbeddedDocument, GetDictMixin):

    reference_id = mongoengine.StringField()
    reference_model = mongoengine.StringField()
    reference_name = mongoengine.StringField()
    reference_filter = mongoengine.StringField()

    def __unicode__(self):
        return self.reference_filter


class AnnotationType(mongoengine.Document, GetDictMixin):

    annotation_type = mongoengine.StringField()

    def __unicode__(self):
        return self.annotation_type

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_type', kwargs={'pk': self.pk})


class AnnotationCategory(mongoengine.Document, GetDictMixin):

    category = mongoengine.StringField()
    annotation_type = mongoengine.ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.category

    def get_absolute_url(self):
        return reverse(
            'lizard_annotation_api_category',
            kwargs={'pk': self.pk},
        )


class AnnotationStatus(mongoengine.Document, GetDictMixin):

    status = mongoengine.StringField()
    annotation_type = mongoengine.ReferenceField(AnnotationType)

    def __unicode__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('lizard_annotation_api_status', kwargs={'pk': self.pk})


class Annotation(mongoengine.Document, GetDictMixin):
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
