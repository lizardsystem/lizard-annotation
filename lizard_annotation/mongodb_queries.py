# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from lizard_annotation.models import AnnotationCategory
from lizard_annotation.models import AnnotationType
from lizard_annotation.models import AnnotationStatus
from lizard_annotation.models import Annotation
from lizard_annotation.models import ReferenceObject

from datetime import datetime


def remove_all_data():
    Annotation.objects.delete()
    AnnotationCategory.objects.delete()
    AnnotationStatus.objects.delete()
    AnnotationType.objects.delete()


def insert_dummy_data():
    insert_dummy_annotationtypes()
    insert_dummy_annotationstatuses()
    insert_dummy_categories()
    insert_dummy_annotations()


def insert_dummy_categories():
    annotation_type = AnnotationType.objects.filter(**{
                    "annotation_type": "interpretatie"})[0]
    categories = [
        {
            "category": "Ecologie",
            "annotation_type": annotation_type,
        },
        {
            "category": "onderzoek Kwantiteit",
            "annotation_type": annotation_type,
        },
        {
            "category": "In",
            "annotation_type": annotation_type,
        },
        {
            "category": "Algemeen",
            "annotation_type": annotation_type,
        },
        {
            "category": "Waterkwaliteit",
            "annotation_type": annotation_type,
        }]

    for item in categories:
        obj = AnnotationCategory(**item)
        obj.save()


def insert_dummy_annotationtypes(annotation_types=None):
    """ Expects a list with strings if not uses
    dummy list."""
    if not isinstance(annotation_types, list):
        annotation_types = ["interpretatie",
                            "actie",
                            "veldwaarneming"]
    for item in annotation_types:
        obj = AnnotationType()
        obj.annotation_type = item
        obj.save()


def insert_dummy_annotationstatuses():
    annotationtype_interp = AnnotationType.objects.filter(**{
            "annotation_type": "interpretatie"})[0]
    annotationtype_action = AnnotationType.objects.filter(**{
            "annotation_type": "actie"})[0]
    statuses = [
        {
            "status": "In bewerking",
            "annotation_type": annotationtype_interp,
        },
        {
            "status": "Concept",
            "annotation_type": annotationtype_interp,
        },
        {
            "status": "Bewerking",
            "annotation_type": annotationtype_interp,
        },
        {
            "status": "Definitief",
            "annotation_type": annotationtype_interp,
        },
        {
            "status": "Afgehandeld",
            "annotation_type": annotationtype_action,
        }]

    for item in statuses:
        obj = AnnotationStatus(**item)
        obj.save()


def insert_dummy_annotations():

    obj_a = ReferenceObject()
    obj_a.reference_id = 100
    obj_a.reference_model = "Gebied"
    obj_a.reference_name = "Aan-afvoergebied A"
    obj_a.reference_filter = "%s%d" % (obj_a.reference_model,
                                       obj_a.reference_id)

    obj_b = ReferenceObject()
    obj_b.reference_id = 200
    obj_b.reference_model = "Gebied"
    obj_b.reference_name = "Aan-afvoergebied B"
    obj_b.reference_filter = "%s%d" % (obj_b.reference_model,
                                       obj_b.reference_id)

    annotations = [
        {
            "title": "Licht doorlatenheid en milieu vriendelijke oevers",
            "status": AnnotationStatus.objects.filter(**{
                    "status": "In bewerking"})[0],
            "annotation_type": AnnotationType.objects.filter(**{
                    "annotation_type": "interpretatie"})[0],
            "category":  AnnotationCategory.objects.filter(**{
                    "category": "Ecologie"})[0],
            "user_creator": "Alexandr",
            "dt_creation": datetime.today(),
            "period_start": datetime.today(),
            "period_end": None,
            "reference_objects": {
                obj_a.reference_filter: obj_a,
                obj_b.reference_filter: obj_b},
        },
        {
            "title": "Kroos",
            "status": AnnotationStatus.objects.filter(**{
                    "status": "Concept"})[0],
            "annotation_type": AnnotationType.objects.filter(**{
                    "annotation_type": "interpretatie"})[0],
            "category":  AnnotationCategory.objects.filter(**{
                    "category": "onderzoek Kwantiteit"})[0],
            "user_creator": "Alexandr",
            "dt_creation": datetime.today(),
            "period_start": datetime.today(),
            "period_end": None,
            "reference_objects": {obj_a.reference_filter: obj_a},
        },
    ]

    for item in annotations:
        annotation = Annotation(**item)
        annotation.save()


def annotations_list(reference_filter):
    if reference_filter:
        key = "reference_objects__%s" % reference_filter
        f = {key: {"$exists": True}}
        return Annotation.objects(**f)
    else:
        return Annotation.objects[:1]
