from django.contrib import admin
from django.contrib.contenttypes import generic

from lizard_annotation.models import (
    Annotation,
    AnnotationCategory,
    AnnotationStatus,
    AnnotationType,
    ReferenceObject,
)


class ReferenceObjectInline(admin.TabularInline):
    model = ReferenceObject

class AnnotationAdmin(admin.ModelAdmin):
    inlines = [
        ReferenceObjectInline,
    ]


admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(AnnotationStatus)
admin.site.register(AnnotationCategory)
admin.site.register(AnnotationType)
