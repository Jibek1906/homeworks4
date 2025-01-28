from django.db import models

class RecipeModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='название рецепта')
    description = models.TextField(verbose_name='описание рецепта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

class IngredientModel(models.Model):
    Unit_Of_Measurement = (
        ('грамм', 'грамм'),
        ('килограмм', 'килограмм'),
        ('миллилитр', 'миллилитр'),
        ('литр', 'литр'),
        ('штук', 'штук'),
    )
    name = models.CharField(max_length=100, verbose_name='название ингридиента')
    quantity = models.PositiveIntegerField(verbose_name='количество')
    unit = models.CharField(max_length=100, choices=Unit_Of_Measurement, verbose_name='единица измерения')
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ингридиент'
        verbose_name_plural = 'ингридиенты'
