# Generated by Django 5.1.4 on 2025-01-28 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0004_rename_ingredient_ingredientmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientmodel',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='cooking.recipemodel'),
        ),
    ]
