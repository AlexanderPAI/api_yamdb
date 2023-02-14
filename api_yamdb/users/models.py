from django.contrib.auth.models import AbstractUser
from django.db import models

# Пока хер его знает, как реализовывать права,
# изначально предполагал, что буду делать через permissions.
# Через админку кастомная модель работает. Для разработки моделей Сёмы пока хватит.
# Это заглушка, пока не разберусь, что делать с choices.
ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Админ'),
)


class User(AbstractUser):
    """Кастомная модель пользователя"""
    email = models.EmailField(
        blank=True,
        verbose_name='Электронная почта',
    )
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='user',
        verbose_name='Роль',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
    
    def __str__(self):
        return self.username
