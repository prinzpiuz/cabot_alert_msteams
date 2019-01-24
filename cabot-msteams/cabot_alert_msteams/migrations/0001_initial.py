# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabotapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSTeamsAlert',
            fields=[
                ('alertplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cabotapp.AlertPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cabotapp.alertplugin',),
        ),
        migrations.CreateModel(
            name='MSTeamsAlertUserData',
            fields=[
                ('alertpluginuserdata_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cabotapp.AlertPluginUserData')),
                ('msteams_alias', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cabotapp.alertpluginuserdata',),
        ),
    ]