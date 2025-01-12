from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('Детектив', 'Детектив'),
        ('Романтика', 'Романтика'),
        ('Фантастика', 'Фантастика'),
    )
    image = models.ImageField(upload_to='movies/', verbose_name='загрузите фото', null=True)
    title = models.CharField(max_length=100, verbose_name='напишите название книги', null=True)
    description = models.TextField(verbose_name='укажите описание книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=800)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES, 
                                     verbose_name='выберите жанр')
    mail = models.EmailField(unique=True, verbose_name='укажите email')
    director = models.CharField(max_length=100, verbose_name='укажите автора',
                                default='Джоан Роулинг', null=True)
    trailer = models.URLField(verbose_name='укажите ссылку с YouTube', null=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Список книг'

    def __str__(self):
        return f"{self.title} - {self.price} сом"

class Reviews(models.Model):
    STARS = (
        ('⭐️', '⭐️'),
        ('⭐️⭐️', '⭐️⭐️'),
        ('⭐️⭐️⭐️', '⭐️⭐️⭐️'),
        ('⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️'),
        ('⭐️⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️⭐️'),
    )
    reviews_choice = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='books', verbose_name='выберите книгу для отзыва')
    created_at = models.DateField(auto_now_add=True)
    comment = models.TextField(verbose_name='комментарий')
    stars = models.CharField(max_length=100, choices=STARS, default='⭐️⭐️⭐️⭐️⭐️', verbose_name='оценка')

    def __str__(self):
        return f"{self.comment} - {self.stars }"

    class Meta:
        verbose_name='комментарий'
        verbose_name_plural='коментарии'