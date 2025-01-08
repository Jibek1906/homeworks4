# Generated by Django 5.1.4 on 2025-01-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='movies/', verbose_name='загрузите фото')),
                ('title', models.CharField(max_length=100, verbose_name='напишите название фильма')),
                ('description', models.TextField(blank=True, verbose_name='укажите описание книги')),
                ('price', models.PositiveIntegerField(default=800, verbose_name='укажите цену')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genre_choices', models.CharField(choices=[('Детектив', 'Детектив'), ('Романтика', 'Романтика'), ('Фантастика', 'Фантастика')], max_length=100, verbose_name='выберите жанр')),
                ('mail', models.EmailField(max_length=254, unique=True, verbose_name='укажите email')),
                ('director', models.CharField(default='Джоан Роулинг', max_length=100, verbose_name='укажите режисера')),
                ('trailer', models.URLField(verbose_name='укажите ссылку с YouTube')),
            ],
        ),
    ]