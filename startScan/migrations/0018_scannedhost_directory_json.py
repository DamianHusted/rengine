# Generated by Django 3.0.7 on 2020-07-02 13:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0017_waybackendpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='scannedhost',
            name='directory_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
            preserve_default=False,
        ),
    ]
