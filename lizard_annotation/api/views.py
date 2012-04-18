# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
"""
API views not coupled to models.
"""

from django.core.urlresolvers import reverse

from djangorestframework.response import Response
from djangorestframework.views import View
from djangorestframework import status

from lizard_annotation.models import (
    Annotation,
    AnnotationType,
    AnnotationStatus,
    AnnotationCategory,
)

from lizard_annotation.forms import (
    AnnotationForm,
    StatusForm,
    CategoryForm,
    TypeForm,
)

from django.contrib.contenttypes.models import ContentType
from lizard_area.models import Area
from lizard_api.base import BaseApiView

"""
Beware that the djangorestframework trips if you name an attribute of
the view 'model', and also if one of the methods return a dict with a key
'model' in it. Hence the attribute 'document' on a number of classes
"""

def _update_mongoengine_document(obj, content):
    """
    Update fields from obj with values from content.
    """
    for key in content:
        if key in obj:
            obj[key] = content[key]


class RootView(View):
    """
    Startpoint.
    """
    def get(self, request):
        if request.user.is_anonymous():
            return Response(status.HTTP_403_FORBIDDEN)

        return {
            "annotations grid": reverse(
                'lizard_annotation_api_annotation_grid'),
            "annotations": reverse(
                'lizard_annotation_api_annotation_root'),
            "annotation statuses": reverse(
                'lizard_annotation_api_annotation_status_root'),
            "annotation categories": reverse(
                'lizard_annotation_api_annotation_category_root'),
            "annotation types": reverse(
                'lizard_annotation_api_annotation_type_root'),
            }


class AnnotationGridView(View):
    """
    Show a (filtered) list of annotations with all annotation
    fields.

    Possible filters are:

    - annotation_type
    - object_ident
    """
    def get(self, request):
        """
        Return annotationgrid.

        TODO Add some pagination if the grid gets really long.
        """
        if request.user.is_anonymous():
            return Response(status.HTTP_403_FORBIDDEN)

        annotations = Annotation.objects.all()

        # Handle additional filtering
        annotation_type = request.GET.get('type')
        if annotation_type:
            try:
                type_obj = AnnotationType.objects.get(
                    annotation_type=annotation_type)
            except AnnotationType.DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)
            annotations = annotations.filter(annotation_type=type_obj)

        # Special case for annotations with area objects
        area_ident = request.GET.get('object_ident')
        area_ct= ContentType.objects.get_for_model(Area)
        if area_ident:
            try:
                area = Area.objects.get(ident=area_ident)
            except Area.DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)
            annotations = area.annotation_set.all()
                

        return {'annotations': [a.get_dict()
                                for a in annotations]}


class DocumentRootView(View):
    """
    Baseview for root views.

    Subclasses must set the document attribute.
    """
    def get(self, request):
        """
        Read a document list. Assumes documents have a get_absolute_url()
        method implemented.
        """
        if request.user.is_anonymous():
            return Response(status.HTTP_403_FORBIDDEN)

        return [[d, d.get_absolute_url()]
                for d in self.document.objects.all()]

    def post(self, request, pk=None):
        """Create a document."""
        if request.user.is_anonymous():
            return Response(status.HTTP_403_FORBIDDEN)

        self.document(**self.CONTENT).save()
        return Response(status.HTTP_200_OK)


class AnnotationRootView(DocumentRootView):
    """
    View all annotations or create one.
    """
    document = Annotation
    form = AnnotationForm


class AnnotationTypeRootView(DocumentRootView):
    """
    View all types or create one.
    """
    document = AnnotationType
    form = TypeForm


class AnnotationCategoryRootView(DocumentRootView):
    """
    View all categories or create one.
    """
    document = AnnotationCategory
    form = CategoryForm


class AnnotationStatusRootView(DocumentRootView):
    """
    View all statuses or create one.
    """
    document = AnnotationStatus
    form = StatusForm


class DocumentView(View):
    """
    Baseview for detail views.

    Subclasses must set form and document attributes.
    """
    def get(self, request, pk):
        """Read a document."""
        if request.user.is_anonymous():
            return Response(status.HTTP_403_FORBIDDEN)

        try:
            obj = self.document.objects.get(pk=pk)
        except self.document.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        if request.GET.get('_format') == 'property':
            fields = request.GET.get('_fields')
            if fields:
                properties = fields.split(',')
            else:
                properties = None
            property_list = obj.get_property_list(properties=properties)
            return {'properties': property_list}

        return obj.get_dict(ref_urls=True)

    def put(self, request, pk):
        """Update a document."""
        if request.user.is_anonymous():
            return Response(status.HTTP_403_FORBIDDEN)

        try:
            obj = self.document.objects.get(pk=pk)
            _update_mongoengine_document(obj, self.CONTENT)
            obj.save()
            return Response(status.HTTP_200_OK)
        except self.document.DoesNotExist:
            obj = self.document(pk=pk, **self.CONTENT)
            obj.save()
            return Response(status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """Delete a document."""
        if request.user.is_anonymous():
            return Response(status.HTTP_403_FORBIDDEN)

        try:
            self.document.objects.get(pk=pk).delete()
            return Response(status.HTTP_200_OK)
        except self.document.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class AnnotationView(DocumentView):
    """
    Edit annotation details.

    Supply '_format=property' as get parameter to return a property,
    value list. Note that doing so breaks the prefilled forms. To get
    only a selection of fields supply a comma-separated list of the
    form '_fields=property1,property2'.
    """
    document = Annotation
    form = AnnotationForm


class AnnotationTypeView(DocumentView):
    """
    Edit annotation type details.
    """
    document = AnnotationType
    form = TypeForm


class AnnotationCategoryView(DocumentView):
    """
    Edit annotation category details.
    """
    document = AnnotationCategory
    form = CategoryForm


class AnnotationStatusView(DocumentView):
    """
    Edit annotation status details.
    """
    document = AnnotationStatus
    form = StatusForm

# Specialized view for the detailform
class AnnotationFormView(BaseApiView):
    """
    Annotation view for form.
    """
    model_class = Annotation
    name_field = 'title'

    valid_field='valid'
    valid_value=True

    field_mapping = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'datetime_period_start': 'datetime_period_start',
        'datetime_period_end': 'datetime_period_end',
        'geom': 'geom',
        'annotation_status': 'annotation_status',
        'annotation_type': 'annotation_type',
        'annotation_category': 'annotation_category',
        'valid': 'valid',
    }


    def get_object_for_api(self, annotation, flat=True,
                           size=BaseApiView.COMPLETE, include_geom=False):
        """
        create annotation object
        """

        output = {}

        if size == self.ID_NAME:
            output = {
                'id': annotation.id,
                'name': annotation.title,
            }


        if size >= self.SMALL:
            output = {
                'id': annotation.id,
                'title': annotation.title,
                'description': annotation.description,
                'datetime_period_start': annotation.datetime_period_start,
                'datetime_period_end': annotation.datetime_period_end,
                'annotation_status': self._get_related_object(
                    annotation.annotation_status,
                    flat,
                ),
                'annotation_type': self._get_related_object(
                    annotation.annotation_type,
                    flat,
                ),
                'annotation_category': self._get_related_object(
                    annotation.annotation_category,
                    flat,
                ),
                'areas': self._get_related_objects(
                    annotation.areas,
                    flat,
                ),
                'waterbodies': self._get_related_objects(
                    annotation.waterbodies,
                    flat,
                ),
                'measures': self._get_related_objects(
                    annotation.measures,
                    flat,
                ),
                'workspaces': self._get_related_objects(
                    annotation.workspaces,
                    flat,
                ),
                'collages': self._get_related_objects(
                    annotation.collages,
                    flat,
                ),
                'valid': annotation.valid,
            }

        if include_geom:
            output.update({
                'geom': annotation.get_geometry_wkt_string(),
            })
            

        return output

    def update_many2many(self, record, model_field, linked_records):
        """
        update specific part of manyToMany relations.
        input:
        - record: annotation
        - model_field. many2many field object
        - linked_records. list with dictionaries with:
            id: id of related objects
            optional some relations in case the relation is through
            another object
        """
        self.save_single_many2many_relation(record,
            model_field,
            linked_records,
        )
