from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class Choices(models.TextChoices):
    USER = 'user', 'user'
    MODERATOR = 'moderator', 'moderator'
    ADMIN = 'admin', 'admin'


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        db_index=True,
        verbose_name='Email',
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # документация (https://docs.djangoproject.com/en/3.1/topics/auth/
    # customizing/#writing-a-manager-for-a-custom-user-model)
    # на практике, без менеджера тесты пройдет, но суперюзера не даст создать
    objects = UserManager()

    role = models.TextField(
        max_length=200,
        choices=Choices.choices,
        default=Choices.USER,
        verbose_name='Пользовательская роль',
    )
    username = models.CharField(
        unique=True,
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Имя пользователя',
    )
    is_active = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    first_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Фамилия',
    )
    confirmation_code = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Код подтверждения',
    )

    def save(self, *args, **kwargs):
        self.is_active = True
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['email']
