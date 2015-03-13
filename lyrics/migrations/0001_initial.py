# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('spotify_url', models.URLField()),
                ('spotify_href', models.URLField()),
                ('cover_url', models.URLField(null=True)),
                ('cover_thumb_url', models.URLField(null=True)),
                ('album_type', models.CharField(max_length=100)),
                ('artists', models.ManyToManyField(to='shows.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('lyrics', models.TextField()),
                ('milliseconds', models.IntegerField()),
                ('album', models.ForeignKey(related_name='tracks', to='lyrics.Album')),
            ],
            options={
                'ordering': ('number',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='song',
            unique_together=set([('album', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('name', 'spotify_url', 'spotify_href')]),
        ),
    ]
