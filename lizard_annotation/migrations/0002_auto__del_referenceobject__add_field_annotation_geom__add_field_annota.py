# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ReferenceObject'
        db.delete_table('lizard_annotation_referenceobject')

        # Adding field 'Annotation.geom'
        db.add_column('lizard_annotation_annotation', 'geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True), keep_default=False)

        # Adding field 'Annotation.valid'
        db.add_column('lizard_annotation_annotation', 'valid', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding M2M table for field areas on 'Annotation'
        db.create_table('lizard_annotation_annotation_areas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('annotation', models.ForeignKey(orm['lizard_annotation.annotation'], null=False)),
            ('area', models.ForeignKey(orm['lizard_area.area'], null=False))
        ))
        db.create_unique('lizard_annotation_annotation_areas', ['annotation_id', 'area_id'])

        # Adding M2M table for field waterbodies on 'Annotation'
        db.create_table('lizard_annotation_annotation_waterbodies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('annotation', models.ForeignKey(orm['lizard_annotation.annotation'], null=False)),
            ('waterbody', models.ForeignKey(orm['lizard_measure.waterbody'], null=False))
        ))
        db.create_unique('lizard_annotation_annotation_waterbodies', ['annotation_id', 'waterbody_id'])

        # Adding M2M table for field workspaces on 'Annotation'
        db.create_table('lizard_annotation_annotation_workspaces', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('annotation', models.ForeignKey(orm['lizard_annotation.annotation'], null=False)),
            ('layerworkspace', models.ForeignKey(orm['lizard_workspace.layerworkspace'], null=False))
        ))
        db.create_unique('lizard_annotation_annotation_workspaces', ['annotation_id', 'layerworkspace_id'])

        # Adding M2M table for field collages on 'Annotation'
        db.create_table('lizard_annotation_annotation_collages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('annotation', models.ForeignKey(orm['lizard_annotation.annotation'], null=False)),
            ('layercollage', models.ForeignKey(orm['lizard_workspace.layercollage'], null=False))
        ))
        db.create_unique('lizard_annotation_annotation_collages', ['annotation_id', 'layercollage_id'])


    def backwards(self, orm):
        
        # Adding model 'ReferenceObject'
        db.create_table('lizard_annotation_referenceobject', (
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('annotation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_annotation.Annotation'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('lizard_annotation', ['ReferenceObject'])

        # Deleting field 'Annotation.geom'
        db.delete_column('lizard_annotation_annotation', 'geom')

        # Deleting field 'Annotation.valid'
        db.delete_column('lizard_annotation_annotation', 'valid')

        # Removing M2M table for field areas on 'Annotation'
        db.delete_table('lizard_annotation_annotation_areas')

        # Removing M2M table for field waterbodies on 'Annotation'
        db.delete_table('lizard_annotation_annotation_waterbodies')

        # Removing M2M table for field workspaces on 'Annotation'
        db.delete_table('lizard_annotation_annotation_workspaces')

        # Removing M2M table for field collages on 'Annotation'
        db.delete_table('lizard_annotation_annotation_collages')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'annotation_set'", 'blank': 'True', 'to': "orm['lizard_area.Area']"}),
            'collages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'annotation_set'", 'blank': 'True', 'to': "orm['lizard_workspace.LayerCollage']"}),
            'datetime_period_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'datetime_period_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'waterbodies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'annotation_set'", 'blank': 'True', 'to': "orm['lizard_measure.WaterBody']"}),
            'workspaces': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'annotation_set'", 'blank': 'True', 'to': "orm['lizard_workspace.LayerWorkspace']"})
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
        'lizard_area.area': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Area', '_ormbases': ['lizard_area.Communique']},
            'area_class': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'communique_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_area.Communique']", 'unique': 'True', 'primary_key': 'True'}),
            'data_administrator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.DataAdministrator']", 'null': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'dt_created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 12, 13, 42, 14, 652722)'}),
            'dt_latestchanged': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dt_latestsynchronized': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Area']", 'null': 'True', 'blank': 'True'})
        },
        'lizard_area.communique': {
            'Meta': {'object_name': 'Communique', '_ormbases': ['lizard_geo.GeoObject']},
            'areasort': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'areasort_krw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'dt_latestchanged_krw': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'edited_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'edited_by': ('django.db.models.fields.TextField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'geoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_geo.GeoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'surface': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'watertype_krw': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'lizard_area.dataadministrator': {
            'Meta': {'object_name': 'DataAdministrator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_geo.geoobject': {
            'Meta': {'object_name': 'GeoObject'},
            'geo_object_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_geo.GeoObjectGroup']"}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'lizard_geo.geoobjectgroup': {
            'Meta': {'object_name': 'GeoObjectGroup'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'source_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_map.backgroundmap': {
            'Meta': {'ordering': "('index',)", 'object_name': 'BackgroundMap'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'google_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'is_base_layer': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'layer_names': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'layer_type': ('django.db.models.fields.IntegerField', [], {}),
            'layer_url': ('django.db.models.fields.CharField', [], {'default': "'http://tile.openstreetmap.nl/tiles/${z}/${x}/${y}.png'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'lizard_map.workspacestorage': {
            'Meta': {'object_name': 'WorkspaceStorage'},
            'absolute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'background_map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_map.BackgroundMap']", 'null': 'True', 'blank': 'True'}),
            'custom_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dt_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dt_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'td': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'td_end': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'td_start': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'default': '1254790'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'default': '-14675'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'default': '6964942'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'default': '6668977'})
        },
        'lizard_measure.krwstatus': {
            'Meta': {'object_name': 'KRWStatus'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valid': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'lizard_measure.krwwatertype': {
            'Meta': {'object_name': 'KRWWatertype'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valid': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'watertype_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'watertypes'", 'null': 'True', 'to': "orm['lizard_measure.WatertypeGroup']"})
        },
        'lizard_measure.waterbody': {
            'Meta': {'ordering': "('area',)", 'object_name': 'WaterBody'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'water_bodies'", 'null': 'True', 'to': "orm['lizard_area.Area']"}),
            'area_ident': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'krw_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_measure.KRWStatus']", 'null': 'True', 'blank': 'True'}),
            'krw_watertype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_measure.KRWWatertype']", 'null': 'True', 'blank': 'True'})
        },
        'lizard_measure.watertypegroup': {
            'Meta': {'object_name': 'WatertypeGroup'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lizard_security.dataset': {
            'Meta': {'ordering': "['name']", 'object_name': 'DataSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        'lizard_workspace.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'lizard_workspace.layer': {
            'Meta': {'object_name': 'Layer'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.Category']", 'null': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'filter': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_base_layer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_clickable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_local_server': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'js_popup_class': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'layers': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'location_filter': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'ollayer_class': ('django.db.models.fields.CharField', [], {'default': "'OpenLayers.Layer.WMS'", 'max_length': '80'}),
            'options': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'null': 'True', 'blank': 'True'}),
            'owner_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'request_params': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'null': 'True', 'blank': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.WmsServer']", 'null': 'True', 'blank': 'True'}),
            'single_tile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'source_ident': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lizard_workspace.Tag']", 'null': 'True', 'blank': 'True'}),
            'use_location_filter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'lizard_workspace.layercollage': {
            'Meta': {'object_name': 'LayerCollage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.Category']", 'null': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lizard_workspace.Layer']", 'null': 'True', 'through': "orm['lizard_workspace.LayerCollageItem']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'owner_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'personal_category': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'lizard_workspace.layercollageitem': {
            'Meta': {'ordering': "('grouping_hint', 'name')", 'object_name': 'LayerCollageItem'},
            'grouping_hint': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.Layer']"}),
            'layer_collage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.LayerCollage']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'lizard_workspace.layerworkspace': {
            'Meta': {'ordering': "['name']", 'object_name': 'LayerWorkspace', '_ormbases': ['lizard_map.WorkspaceStorage']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.Category']", 'null': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'layers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lizard_workspace.Layer']", 'null': 'True', 'through': "orm['lizard_workspace.LayerWorkspaceItem']", 'blank': 'True'}),
            'owner_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'personal_category': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'workspacestorage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_map.WorkspaceStorage']", 'unique': 'True', 'primary_key': 'True'})
        },
        'lizard_workspace.layerworkspaceitem': {
            'Meta': {'object_name': 'LayerWorkspaceItem'},
            'clickable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'filter_string': ('django.db.models.fields.CharField', [], {'max_length': '124', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.Layer']"}),
            'layer_workspace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_workspace.LayerWorkspace']"}),
            'opacity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'lizard_workspace.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'lizard_workspace.wmsserver': {
            'Meta': {'object_name': 'WmsServer'},
            'abstract': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'enable_proxy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_clickable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_local_server': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'js_popup_class': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ws_prefix': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lizard_annotation']
