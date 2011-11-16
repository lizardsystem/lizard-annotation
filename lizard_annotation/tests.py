# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

import logging
import mongoengine
from django.test import TestCase

from lizard_annotation import models as m
from lizard_annotation import mongodb_queries as qrs

logger = logging.getLogger(__name__)


class TransactionTest(TestCase):

    def setUp(self):
        """
        Clear the collections in the testdatabase.
        """
        qrs.remove_all_data()
        qrs.insert_dummy_data()

    def test_annotation_types_published_1(self):
        """ Tests inserting annotation types function with out args."""
        qrs.insert_dummy_annotationtypes()
        self.assertNotEqual(len(m.AnnotationType.objects()), 0)

    def test_annotation_types_published_2(self):
        """ Tests inserting annotation types function with args."""
        annotation_types = ["type_1", "type_2"]
        qrs.insert_dummy_annotationtypes(annotation_types)
        self.assertEqual(len(m.AnnotationType.objects(
                    annotation_type=annotation_types[0])), 1)

    def test_annotation_statuses_published(self):
        """ Tests inserting annotation statuses."""
        qrs.insert_dummy_annotationtypes()
        qrs.insert_dummy_annotationstatuses()
        self.assertNotEqual(len(m.AnnotationStatus.objects()), 0)

    def test_annotation_categories_published(self):
        """ Tests inserting annotation categories."""
        qrs.insert_dummy_annotationtypes()
        qrs.insert_dummy_categories()
        self.assertNotEqual(len(m.AnnotationCategory.objects()), 0)

    def test_annotations_published(self):
        """ Tests inserting annotations."""
        self.assertNotEqual(len(m.Annotation.objects()), 0)

    def tearDown(self):
        """
        Clear the collections in the testdatabase.
        """
        qrs.remove_all_data()
