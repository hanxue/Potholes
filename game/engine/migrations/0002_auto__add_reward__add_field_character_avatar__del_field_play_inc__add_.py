# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Reward'
        db.create_table('engine_reward', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Character'])),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Play'])),
            ('attr', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('point', self.gf('django.db.models.fields.IntegerField')()),
            ('inc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('inf', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('limit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('engine', ['Reward'])

        # Adding field 'Character.avatar'
        db.add_column('engine_character', 'avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True), keep_default=False)

        # Deleting field 'Play.inc'
        db.delete_column('engine_play', 'inc')

        # Adding field 'Play.dt'
        db.add_column('engine_play', 'dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2011, 7, 30, 0, 11, 16, 735411), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Reward'
        db.delete_table('engine_reward')

        # Deleting field 'Character.avatar'
        db.delete_column('engine_character', 'avatar')

        # Adding field 'Play.inc'
        db.add_column('engine_play', 'inc', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Play.dt'
        db.delete_column('engine_play', 'dt')


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
        'engine.character': {
            'Meta': {'object_name': 'Character'},
            'action': ('django.db.models.fields.IntegerField', [], {}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'experience': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'engine.play': {
            'Meta': {'object_name': 'Play'},
            'attr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['engine.Character']"}),
            'point': ('django.db.models.fields.IntegerField', [], {})
        },
        'engine.reward': {
            'Meta': {'object_name': 'Reward'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['engine.Play']"}),
            'attr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'inc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'inf': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'limit': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['engine.Character']"}),
            'point': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['engine']
