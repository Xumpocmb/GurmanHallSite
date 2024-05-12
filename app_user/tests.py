from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from app_user.models import User, EmailVerification


class TestUser(TestCase):
    def test_user_registration_get(self):
        url = reverse('app_user:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_registration_post(self):
        data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@x.com',
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }

        url = reverse('app_user:register')
        response = self.client.post(url, data)

        username = data['username']
        self.assertTrue(User.objects.filter(username=username).exists())

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('app_home:home'))

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(email_verification.first().user.username, username)
        self.assertEqual(email_verification.first().expired.date(),
                         (timezone.now() + timezone.timedelta(hours=48)).date())

    def test_user_registration_post_invalid_data(self):
        data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@x.com',
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword2'
        }

        user = User.objects.create_user(data['username'])

        url = reverse('app_user:register')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_user/register.html')
        # self.assertContains(response, 'Пароли не совпадают')
        self.assertContains(response, 'существует')
