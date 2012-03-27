# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from lizard_annotation.models import AnnotationCategory
from lizard_annotation.models import AnnotationType
from lizard_annotation.models import AnnotationStatus
from lizard_annotation.models import Annotation
from lizard_annotation.models import ReferenceObject

from datetime import datetime
from datetime import timedelta

SOME_LONGER_TEXT = (
    '<p>Lorem ipsum dolor sit amet, consectetur adipiscing'
    'elit. Integer nec odio. Praesent libero. Sed cursus ante'
    'dapibus diam. Sed nisi. <b>Nulla</b> <i>quis</i> sem at'
    'nibh elementum imperdiet. Duis sagittis ipsum. Praesent'
    'mauris. Fusce nec tellus sed augue semper porta. Mauris'
    'massa. Vestibulum lacinia arcu eget nulla. Class aptent'
    'taciti sociosq.</p>')


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
                    'annotation_type': 'interpretatie'})[0]
    categories = [
        {
            'annotation_category': 'Ecologie',
            'annotation_type': annotation_type,
        },
        {
            'annotation_category': 'onderzoek Kwantiteit',
            'annotation_type': annotation_type,
        },
        {
            'annotation_category': 'In',
            'annotation_type': annotation_type,
        },
        {
            'annotation_category': 'Algemeen',
            'annotation_type': annotation_type,
        },
        {
            'annotation_category': 'Waterkwaliteit',
            'annotation_type': annotation_type,
        }]

    for item in categories:
        obj = AnnotationCategory(**item)
        obj.save()


def insert_dummy_annotationtypes(annotation_types=None):
    ''' Expects a list with strings if not uses
    dummy list.'''
    if not isinstance(annotation_types, list):
        annotation_types = ['interpretatie',
                            'actie',
                            'veldwaarneming']
    for item in annotation_types:
        obj = AnnotationType()
        obj.annotation_type = item
        obj.save()


def insert_dummy_annotationstatuses():
    annotationtype_interp = AnnotationType.objects.filter(**{
            'annotation_type': 'interpretatie'})[0]
    annotationtype_action = AnnotationType.objects.filter(**{
            'annotation_type': 'actie'})[0]
    statuses = [
        {
            'annotation_status': 'In bewerking',
            'annotation_type': annotationtype_interp,
        },
        {
            'annotation_status': 'Concept',
            'annotation_type': annotationtype_interp,
        },
        {
            'annotation_status': 'Bewerking',
            'annotation_type': annotationtype_interp,
        },
        {
            'annotation_status': 'Definitief',
            'annotation_type': annotationtype_interp,
        },
        {
            'annotation_status': 'Afgehandeld',
            'annotation_type': annotationtype_action,
        }]

    for item in statuses:
        obj = AnnotationStatus(**item)
        obj.save()


def insert_dummy_annotations():

    annotations = [{
        'title': 'Licht doorlatenheid en milieu vriendelijke oevers',
        'description': SOME_LONGER_TEXT,
        'annotation_status': AnnotationStatus.objects.get(
            annotation_status='In bewerking'),
        'annotation_type': AnnotationType.objects.get(
            annotation_type='interpretatie'),
        'annotation_category': AnnotationCategory.objects.get(
            annotation_category='Ecologie'),
    },
    {
        'title': 'Kroos',
        'description': SOME_LONGER_TEXT,
        'annotation_status': AnnotationStatus.objects.get(
            annotation_status='Concept'),
        'annotation_type': AnnotationType.objects.get(
            annotation_type='interpretatie'),
        'annotation_category': AnnotationCategory.objects.get(
            annotation_category='onderzoek Kwantiteit'),
   }]

    for item in annotations:
        annotation = Annotation.objects.create(**item)


def annotations_list(reference_filter):
    if reference_filter:
        key = 'reference_objects__%s' % reference_filter
        f = {key: {'$exists': True}}
        return Annotation.objects(**f)
    else:
        return Annotation.objects[:1]
