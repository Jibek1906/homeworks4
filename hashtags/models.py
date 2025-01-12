from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='название тега')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта')
    price = models.PositiveIntegerField(default=100, verbose_name='цена')
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name
