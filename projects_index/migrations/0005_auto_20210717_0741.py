# Generated by Django 3.1.4 on 2021-07-16 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_index', '0004_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]