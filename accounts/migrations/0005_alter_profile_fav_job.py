# Generated by Django 3.2.7 on 2022-01-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_remove_job_fav_job'),
        ('accounts', '0004_alter_profile_fav_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fav_job',
            field=models.ManyToManyField(to='job.Job'),
        ),
    ]