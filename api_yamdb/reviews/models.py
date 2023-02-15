from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
        help_text='Введите название вашей категории',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Идентификатор категории',
        unique=True,
        max_length=50,
        help_text='(Пример: films)'
    )

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
        help_text='Введите название вашей категории',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Идентификатор категории',
        unique=True,
        max_length=50,
        help_text='(Пример: films)'
    )

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(
        verbose_name='Название произведения',
        help_text='Введите название произведения',
        max_length=256,
    )
    year = models.IntegerField(
        verbose_name='Дата публикации',
    )
    description = models.TextField(
        verbose_name='Описание произведения',
        help_text='Опишите произведение',
        null=True
    )
    categories = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='categories',
        help_text='Выберите категорию',
        blank=True,
        null=True
    )
    genres = models.ForeignKey(
        Genres,
        on_delete=models.SET_NULL,
        verbose_name='Жанр',
        related_name='genre',
        help_text='Выберите жанр',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Reviews(models.Model):
    pass

class Comments(models.Model):
    pass