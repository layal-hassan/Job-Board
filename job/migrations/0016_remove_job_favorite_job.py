# Generated by Django 3.2.7 on 2021-10-20 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_job_favorite_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='favorite_job',
        ),
    ]