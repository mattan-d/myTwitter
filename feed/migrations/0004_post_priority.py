# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20141005_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='priority',
            field=models.PositiveIntegerField(default=3, choices=[(5, b'Very High'), (4, b'High'), (3, b'Normal'), (2, b'Low'), (1, b'Very Low')]),
            preserve_default=True,
        ),
    ]
