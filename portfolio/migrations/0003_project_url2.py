# Generated by Django 5.2.1 on 2025-05-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_technologies_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url2',
            field=models.URLField(blank=True),
        ),
    ]
