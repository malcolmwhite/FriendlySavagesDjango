# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('lyrics', '0004_auto_20150312_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(related_name='songs', to='lyrics.Album'),
            preserve_default=True,
        ),
    ]
