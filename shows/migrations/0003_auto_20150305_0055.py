# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('shows', '0002_auto_20150305_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showlisting',
            name='venue',
            field=models.ForeignKey(to='shows.Venue', null=True),
            preserve_default=True,
        ),
    ]
