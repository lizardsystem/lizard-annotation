from django.contrib import admin
from django.contrib.contenttypes import generic

from lizard_annotation.models import (
    Annotation,
    AnnotationCategory,
    AnnotationStatus,
    AnnotationType,
    ReferenceObject,
)


admin.site.register(Annotation)
admin.site.register(AnnotationStatus)
admin.site.register(AnnotationCategory)
admin.site.register(AnnotationType)
admin.site.register(ReferenceObject)
