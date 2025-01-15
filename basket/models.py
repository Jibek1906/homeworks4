from django.db import models
from library.models import Books

class BasketModel(models.Model):
    DELIVERY_METHOD = (
        ('Самовывоз', 'Самовывоз'),
        ('Доставка на дом', 'Доставка на дом'),
    )
    PAYMENT_METHOD = (
        ('Наличные', 'Наличные'),
        ('Банковская карта', 'Банковская карта'),
        ('Денежный перевод', 'Денежный перевод'),
    )
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='book')
    name = models.CharField(max_length=100, verbose_name='имя')
    number = models.CharField(max_length=11, verbose_name='телефон')
    mail = models.EmailField(verbose_name='email')
    delivery_address = models.TextField(verbose_name='адрес')
    delivery_choice = models.CharField(max_length=100, choices=DELIVERY_METHOD, verbose_name='способ доставки')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD, verbose_name='способ оплаты')
    ordered_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
    
    def __str__(self):
        return f"{self.book} - заказчик: {self.name}"
