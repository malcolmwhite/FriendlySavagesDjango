# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0002_auto_20150312_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(related_name='songs', to='lyrics.Album'),
            preserve_default=True,
        ),
    ]
