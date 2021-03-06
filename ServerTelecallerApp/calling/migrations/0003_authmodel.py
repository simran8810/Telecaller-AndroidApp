# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calling', '0002_usermodel_detailfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('password', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'AuthModel',
            },
            bases=(models.Model,),
        ),
    ]
