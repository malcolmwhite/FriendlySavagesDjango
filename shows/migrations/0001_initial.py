# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowListing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_and_time', models.DateTimeField(verbose_name=b'date and time of show')),
                ('opener', models.CharField(max_length=40)),
                ('ticket_url', models.CharField(max_length=100)),
                ('other_info', models.CharField(max_length=200)),
                ('sold_out', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='showlisting',
            name='venue',
            field=models.ForeignKey(to='shows.Venue'),
            preserve_default=True,
        ),
    ]
