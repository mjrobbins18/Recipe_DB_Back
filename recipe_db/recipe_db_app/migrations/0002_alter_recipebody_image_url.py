# Generated by Django 3.2.7 on 2021-09-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_db_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipebody',
            name='image_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
