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
    categories =[
        {
            "category": "Ecologie",
            "annotation_type": AnnotationType.objects.filter( **{
                    "annotation_type": "interpretatie"} )[0]
        },
        {
            "category": "onderzoek Kwantiteit",
            "annotation_type": AnnotationType.objects.filter( **{
                    "annotation_type": "interpretatie"} )[0]
        },
        {
            "category": "In",
            "annotation_type": AnnotationType.objects.filter( **{
                    "annotation_type": "interpretatie"} )[0]
        },
        {
            "category": "Algemeen",
            "annotation_type": AnnotationType.objects.filter( **{
                    "annotation_type": "interpretatie"} )[0]
        },
        {
            "category": "Waterkwaliteit",
            "annotation_type": AnnotationType.objects.filter( **{
                    "annotation_type": "interpretatie"} )[0]
        }]

    for item in categories:
        obj = AnnotationCategory(**item)
        obj.save()

def insert_dummy_annotationtypes(annotation_types=None):
    if annotation_types is None:
        annotation_types = ["interpretatie",
                            "actie",
                            "veldwaarneming"]
    for item in annotation_types:
        obj = AnnotationType()
        obj.annotation_type = item
        obj.save()

def insert_dummy_annotationstatuses():
    statuses = [
        {
            "status": "In bewerking",
            "annotation_type": AnnotationType.objects.get(
                annotation_type='interpretatie')
        },
        {
            "status": "Concept",
            "annotation_type": AnnotationType.objects.get(
                annotation_type='interpretatie')
        },
        {
            "status": "Bewerking",
            "annotation_type": AnnotationType.objects.get(
                annotation_type='interpretatie')
        },
        {
            "status": "Definitief",
            "annotation_type": AnnotationType.objects.get(
                annotation_type='interpretatie')
        },
        {
            "status": "Afgehandeld",
            "annotation_type": AnnotationType.objects.get(
                annotation_type='actie')
        }]

    for item in statuses:
        obj = AnnotationStatus(**item)
        obj.save()

def insert_dummy_annotations():

    gebied_a = ReferenceObject()
    gebied_a.reference_id = 100
    gebied_a.reference_model = "Gebied"
    gebied_a.filter = "%s%d" % (gebied_a.reference_model, gebied_a.reference_id)

    gebied_b = ReferenceObject()
    gebied_b.reference_id = 200
    gebied_b.reference_model = "Gebied"
    gebied_b.filter = "%s%d" % (gebied_b.reference_model, gebied_b.reference_id)

    annotations = [
        {
        "title": "Licht doorlatenheid en milieu vriendelijke oevers",
        "status": AnnotationStatus.objects.filter( **{
                "status": "In bewerking"} )[0],
        "annotation_type": AnnotationType.objects.filter( **{
                "annotation_type": "interpretatie"} )[0],
        "category":  AnnotationCategory.objects.filter( **{
                "category": "Ecologie"} )[0],
        "user_creator": "Alexandr",
        "dt_creation": datetime.today(),
        "reference_objects": { gebied_a.filter: gebied_a,
                               gebied_b.filter: gebied_b }
        },
        {
        "title": "Kroos",
        "status": AnnotationStatus.objects.filter( **{
                "status": "Concept"} )[0],
        "annotation_type": AnnotationType.objects.filter( **{
                "annotation_type": "interpretatie"} )[0],
        "category":  AnnotationCategory.objects.filter( **{
                "category": "onderzoek Kwantiteit"} )[0],
        "user_creator": "Alexandr",
        "dt_creation": datetime.today(),
        "reference_objects": { gebied_a.filter: gebied_a }
        }
    ]

    for item in annotations:
        annotation = Annotation(**item)
        annotation.save()

def annotations_list(reference_filter):
    key = "reference_objects__%s" % reference_filter

    f = { key: { "$exists": True } }
    return Annotation.objects(**f)

