# Generated by Django 5.1.4 on 2025-01-28 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingridient',
            new_name='Ingredient',
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'ингридиент', 'verbose_name_plural': 'ингридиенты'},
        ),
    ]
