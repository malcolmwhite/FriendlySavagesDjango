# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('image_url', models.URLField()),
                ('thumb_url', models.URLField()),
                ('facebook_tour_dates_url', models.URLField()),
                ('mbid', models.CharField(max_length=40)),
                ('upcoming_events_count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='showlisting',
            options={'ordering': ('datetime',)},
        ),
        migrations.RenameField(
            model_name='showlisting',
            old_name='date_and_time',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='state',
            new_name='region',
        ),
        migrations.RemoveField(
            model_name='showlisting',
            name='opener',
        ),
        migrations.RemoveField(
            model_name='showlisting',
            name='other_info',
        ),
        migrations.RemoveField(
            model_name='showlisting',
            name='sold_out',
        ),
        migrations.AddField(
            model_name='showlisting',
            name='artists',
            field=models.ForeignKey(related_name='artists', to='shows.Artist', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='description',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='facebook_rsvp_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='formatted_datetime',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='formatted_location',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='on_sale_datetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='ticket_status',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='ticket_type',
            field=models.CharField(max_length=40, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='showlisting',
            name='title',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='country',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='showlisting',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='showlisting',
            name='ticket_url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
