# Generated by Django 3.2.7 on 2021-11-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_remove_job_fav_job'),
        ('accounts', '0003_profile_fav_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fav_job',
            field=models.ManyToManyField(to='job.Job'),
        ),
    ]
