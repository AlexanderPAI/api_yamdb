from django.db import models

# Create your models here.

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
    year = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=False
    )
    description = models.TextField(
        verbose_name='Описание произведения',
        help_text='Опишите произведение'
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
        Categories,
        on_delete=models.SET_NULL,
        verbose_name='Жанр',
        related_name='genre',
        help_text='Выберите жанр',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):  # Надо допилить на счет полей: score и review_id(я пока хз, в инете смотрю)
    """Модель отзывов."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        max_length=1000,
        verbose_name='Отзыв',
        help_text='Напишите отзыв к фильму'
    )
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
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        max_length=1700,
        verbose_name='Комментарий',
        help_text='Введите комментарий к фильму'
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


class Rating(models.Model):
    """Модель рейтинга."""
    rate = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )
    story = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
