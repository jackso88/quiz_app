# Generated by Django 3.1.2 on 2020-10-04 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing_apps', '0003_answer_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='is_published',
            new_name='correct',
        ),
    ]
