# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('image_url', models.URLField()),
                ('thumb_url', models.URLField()),
                ('facebook_tour_dates_url', models.URLField(null=True)),
                ('mbid', models.CharField(max_length=40, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShowListing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=400)),
                ('datetime', models.DateTimeField(verbose_name=b'date and time of show')),
                ('formatted_datetime', models.CharField(max_length=200)),
                ('formatted_location', models.CharField(max_length=40)),
                ('ticket_url', models.URLField(null=True)),
                ('ticket_type', models.CharField(max_length=40, null=True)),
                ('ticket_status', models.CharField(max_length=40)),
                ('on_sale_datetime', models.DateTimeField(null=True)),
                ('facebook_rsvp_url', models.URLField()),
                ('description', models.CharField(max_length=200, null=True)),
                ('artists', models.ManyToManyField(to='shows.Artist', null=True)),
            ],
            options={
                'ordering': ('datetime',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='showlisting',
            name='venue',
            field=models.ForeignKey(to='shows.Venue', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='showlisting',
            unique_together=set([('title', 'datetime', 'facebook_rsvp_url')]),
        ),
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together=set([('name',)]),
        ),
    ]
