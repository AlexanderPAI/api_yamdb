from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        unique=True,
    )
    bio = models.TextField(
        'О себе',
        blank=True,
        null=False,
    )
    role = models.CharField(
        'Роль',
        max_length=30,
        choices=ROLES,
        default='user'
    )
    confirmation_code = models.IntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('id',)  # иначе тестах выпадает два Warnings
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user'
            )
        ]

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
