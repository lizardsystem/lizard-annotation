# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

import mongoengine

from django.core.urlresolvers import reverse

from djangorestframework.views import View

from lizard_annotation.models import Annotation
from lizard_annotation.models import AnnotationType
from lizard_annotation.models import AnnotationStatus
from lizard_annotation.models import AnnotationCategory


class RootView(View):
    """
    Startpoint.
    """
    def get(self, request):
        return {
            "annotations": reverse(
                'lizard_annotation_api_annotation_root'),
            "annotation statuses": reverse(
                'lizard_annotation_api_annotation_status_root'),
            "annotation categories": reverse(
                'lizard_annotation_api_annotation_category_root'),
            "annotation types": reverse(
                'lizard_annotation_api_annotation_type_root'),
            }


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
                    'title': annotation.title,
                    'annotation_type': annotation.annotation_type,
                    'status': annotation.status,
                    'category': annotation.category,
                    'period_start': annotation.period_start,
                    'period_end': annotation.period_end,
                    'user_creator': annotation.user_creator,
                    'id': annotation.id,
                }
                for annotation in annotations]
        }


class AnnotationView(View):
    def get(self, request, pk):
        annotation = Annotation.objects.get(pk=pk)
        result = {}
        for (field_name, field_object) in annotation._fields.items():
            if isinstance(field_object, mongoengine.ReferenceField):
                result[field_name] = {
                    field_name: annotation[field_name],
                    'url': annotation[field_name].get_absolute_url(),
                }
            else:
                result[field_name] = annotation[field_name]
        return result


class AnnotationStatusView(View):
    def get(self, request, pk):
        return AnnotationStatus.objects.get(pk=pk)


class AnnotationStatusRootView(View):
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
