from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


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


class Review(models.Model):
    """Модель отзывов."""
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        max_length=1000,
        verbose_name='Отзыв',
        help_text='Напишите вашу рецензию'
    )
    title = models.ForeignKey(
        Titles,
        verbose_name='Название',
        on_delete=models.CASCADE,
        related_name='titles'
    )
    #score = models.ForeignKey(
    #    validators=(
    #        MinValueValidator(1),
    #        MaxValueValidator(10)
    #    ),
    #    error_messages={'validators': 'Оценка от 1 до 10'}
    #)
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель комментариев."""
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        max_length=1700,
        verbose_name='Комментарий',
        help_text='Введите комментарий отзыву'
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.text
