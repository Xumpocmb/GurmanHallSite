from django.db import models
from time import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', verbose_name='Изображение', null=True, blank=True)
    phone = models.CharField(max_length=12, unique=True, verbose_name='Телефон', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации', null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, verbose_name='Последний вход', null=True, blank=True)
    verified_email = models.BooleanField(default=False, verbose_name='Подтвержденная почта', null=True, blank=True)
    is_archived = models.BooleanField(default=False, verbose_name='Архивирован', null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.username

    def display_id(self):
        return f'ID: {self.id:05}'


class EmailVerification(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    code = models.UUIDField(unique=True, verbose_name='Код подтверждения', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан', null=True, blank=True)
    expired = models.DateTimeField(verbose_name='Действует до', null=True, blank=True)

    class Meta:
        db_table = 'email_verifications'
        verbose_name = 'Подтверждение почты'
        verbose_name_plural = 'Подтверждения почты'
        ordering = ['created']

    def __str__(self):
        return f'Код подтверждения для {self.user.email}'

    def send_verification_email(self):
        link = reverse('app_user:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        full_link = f'{settings.DOMAIN_NAME}{link}'
        send_mail(
            subject='ГурманХол - Регистрация на сайте ',
            message=f'Для подтверждения учетной записи перейдите по ссылке:\n {full_link}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
        )

