# Generated by Django 5.1.4 on 2025-01-15 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0003_rename_books_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
    ]
