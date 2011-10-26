# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

import re
import datetime
import mongoengine

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormMixin

from djangorestframework.response import Response
from djangorestframework.views import View
from djangorestframework import status

from lizard_annotation.models import Annotation
from lizard_annotation.models import AnnotationType
from lizard_annotation.models import AnnotationStatus
from lizard_annotation.models import AnnotationCategory

from lizard_annotation.forms import AnnotationForm

from lizard_annotation.api.utils import unwrap_datetime

import logging
logger = logging.getLogger(__name__)


class RootView(View):
    """
    Startpoint.
    """
    def get(self, request):
        return {
            "annotations grid": reverse(
                'lizard_annotation_api_annotation_root'),
            "annotations": reverse(
                'lizard_annotation_api_annotation_grid'),
            "annotation statuses": reverse(
                'lizard_annotation_api_annotation_status_root'),
            "annotation categories": reverse(
                'lizard_annotation_api_annotation_category_root'),
            "annotation types": reverse(
                'lizard_annotation_api_annotation_type_root'),
            }


class AnnotationGridView(View):
    """
    Show a complete list of all annotations with all annotation
    fields.
    """
        
    def get(self, request):
        """
        Return annotationgrid.

        TODO Add some pagination if the grid gets really long.
        """
        annotation_type = request.GET.get('type')

        # Handle additional filtering
        if annotation_type:
            try:
                type_obj = AnnotationType.objects.get(
                    annotation_type=annotation_type)
            except DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)
            annotations = Annotation.objects.filter(
                annotation_type=type_obj)
        else:
            annotations = Annotation.objects.all()

        return {'annotations': [
            dict([('url', a.get_absolute_url())] +
                 [(k, a[k]) for k in a])
            for a in annotations]}


class AnnotationRootView(View):
    def get(self, request):
        """
        Return annotationlist.
        """
        annotation_type = request.GET.get('type')
        if annotation_type:
            type_obj = AnnotationType.objects.get(
                annotation_type=annotation_type)
            annotations = Annotation.objects.filter(
                annotation_type=type_obj)
        else:
            annotations = Annotation.objects.all()

        return {
            'annotations': [
                {
                    'url': annotation.get_absolute_url()
                }
                for annotation in annotations]
        }


class AnnotationView(View):
    """
    Detailview for Annotations allowing get and post.
    """
    form = AnnotationForm

    def get(self, request, pk):
        result = {}
        a = Annotation.objects.get(pk=pk)
        obj = dict([(k, a[k]) for k in a])
        obj_unwrapped = unwrap_datetime(obj)
        return obj_unwrapped

    def post(self, request, pk=None):
        Annotation(**self.CONTENT).save()
        
        response = Response(status.HTTP_200_OK)
        return self.render(response) 


class AnnotationStatusView(View):
    def get(self, request, pk):
        return AnnotationStatus.objects.get(pk=pk)


class AnnotationStatusRootView(View):
    """
    Complete list of all annotation statuses.
    """
    def get(self, request):
        """
        Return annotationstatus list.
        """
        return {
            'statuses': [
                {
                    'status': status.status,
                    'url': status.get_absolute_url(),
                }
                for status in AnnotationStatus.objects.all()],
        }


class AnnotationCategoryView(View):
    def get(self, request, pk):
        return AnnotationCategory.objects.get(pk=pk)


class AnnotationCategoryRootView(View):
    """
    Complete list of all annotation categories.
    """
    def get(self, request):
        """
        Return annotationcategory list.
        """
        return {
            'categories': [
                {
                    'category': category.category,
                    'url': category.get_absolute_url(),
                }
                for category in AnnotationCategory.objects.all()],
        }


class AnnotationTypeView(View):
    def get(self, request, pk):
        return AnnotationType.objects.get(pk=pk)


class AnnotationTypeRootView(View):
    """
    Complete list of all annotation types.
    """
    def get(self, request):
        """
        Return annotationtype list.
        """
        return {
            'types': [
                {
                    'type': type.annotation_type,
                    'url': type.get_absolute_url(),
                }
                for type in AnnotationType.objects.all()],
        }
