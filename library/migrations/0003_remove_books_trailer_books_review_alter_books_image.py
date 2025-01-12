# Generated by Django 5.1.4 on 2025-01-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_books_options_alter_books_director_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='trailer',
        ),
        migrations.AddField(
            model_name='books',
            name='review',
            field=models.URLField(null=True, verbose_name='укажите ссылку с YouTube'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='books/', verbose_name='загрузите фото'),
        ),
    ]