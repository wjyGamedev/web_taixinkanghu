# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='mobile_phone_num',
            field=models.BigIntegerField(unique=True),
        ),
    ]
