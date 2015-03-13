# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0003_auto_20150312_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(related_name='song', to='lyrics.Album'),
            preserve_default=True,
        ),
    ]
