# Generated by Django 3.2.7 on 2021-09-30 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_db_app', '0005_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recipe',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_post', to='recipe_db_app.recipe'),
            preserve_default=False,
        ),
    ]
