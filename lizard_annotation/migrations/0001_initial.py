# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AnnotationType'
        db.create_table('lizard_annotation_annotationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('annotation_type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('lizard_annotation', ['AnnotationType'])

        # Adding model 'AnnotationCategory'
        db.create_table('lizard_annotation_annotationcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('annotation_category', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('annotation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_annotation.AnnotationType'], null=True, blank=True)),
        ))
        db.send_create_signal('lizard_annotation', ['AnnotationCategory'])

        # Adding model 'AnnotationStatus'
        db.create_table('lizard_annotation_annotationstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('annotation_status', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('annotation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_annotation.AnnotationType'], null=True, blank=True)),
        ))
        db.send_create_signal('lizard_annotation', ['AnnotationStatus'])

        # Adding model 'ReferenceObject'
        db.create_table('lizard_annotation_referenceobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('annotation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_annotation.Annotation'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('lizard_annotation', ['ReferenceObject'])

        # Adding model 'Annotation'
        db.create_table('lizard_annotation_annotation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('datetime_period_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('datetime_period_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('annotation_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_annotation.AnnotationStatus'], null=True, blank=True)),
            ('annotation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_annotation.AnnotationType'], null=True, blank=True)),
            ('annotation_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_annotation.AnnotationCategory'], null=True, blank=True)),
        ))
        db.send_create_signal('lizard_annotation', ['Annotation'])


    def backwards(self, orm):
        
        # Deleting model 'AnnotationType'
        db.delete_table('lizard_annotation_annotationtype')

        # Deleting model 'AnnotationCategory'
        db.delete_table('lizard_annotation_annotationcategory')

        # Deleting model 'AnnotationStatus'
        db.delete_table('lizard_annotation_annotationstatus')

        # Deleting model 'ReferenceObject'
        db.delete_table('lizard_annotation_referenceobject')

        # Deleting model 'Annotation'
        db.delete_table('lizard_annotation_annotation')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lizard_annotation.annotation': {
            'Meta': {'object_name': 'Annotation'},
            'annotation_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_annotation.AnnotationCategory']", 'null': 'True', 'blank': 'True'}),
            'annotation_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_annotation.AnnotationStatus']", 'null': 'True', 'blank': 'True'}),
            'annotation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_annotation.AnnotationType']", 'null': 'True', 'blank': 'True'}),
            'datetime_period_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'datetime_period_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference_objects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contenttypes.ContentType']", 'through': "orm['lizard_annotation.ReferenceObject']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'lizard_annotation.annotationcategory': {
            'Meta': {'object_name': 'AnnotationCategory'},
            'annotation_category': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'annotation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_annotation.AnnotationType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lizard_annotation.annotationstatus': {
            'Meta': {'object_name': 'AnnotationStatus'},
            'annotation_status': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'annotation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_annotation.AnnotationType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lizard_annotation.annotationtype': {
            'Meta': {'object_name': 'AnnotationType'},
            'annotation_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lizard_annotation.referenceobject': {
            'Meta': {'object_name': 'ReferenceObject'},
            'annotation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_annotation.Annotation']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['lizard_annotation']
