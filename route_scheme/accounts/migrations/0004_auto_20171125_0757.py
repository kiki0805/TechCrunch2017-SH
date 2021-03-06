# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20171125_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='user',
            field=models.ForeignKey(related_name='status', to=settings.AUTH_USER_MODEL),
        ),
    ]
