# Generated by Django 3.1.2 on 2020-10-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_apps', '0002_auto_20201004_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
