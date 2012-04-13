from django.contrib import admin

from lizard_annotation.models import (
    Annotation,
    AnnotationCategory,
    AnnotationStatus,
    AnnotationType,
)


admin.site.register(Annotation)
admin.site.register(AnnotationStatus)
admin.site.register(AnnotationCategory)
admin.site.register(AnnotationType)
