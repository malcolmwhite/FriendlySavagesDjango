# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0005_auto_20150312_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='in_soundbar_playlist',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='stream_href',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
