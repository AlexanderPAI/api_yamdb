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

    class Meta:
        ordering = ['-name']


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

    class Meta:
        ordering = ['-name']


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
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='category',
        help_text='Выберите категорию',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genres,
        verbose_name='Жанр',
        related_name='genre',
        help_text='Выберите жанр',
        through='GenresTitles'
    )

    def __str__(self):
        return self.name


class GenresTitles(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'


class Reviews(models.Model):
    pass

class Comments(models.Model):
    pass