# Generated by Django 3.2.7 on 2021-10-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_db_app', '0008_auto_20211001_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
