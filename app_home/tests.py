from django.test import TestCase

from django.urls import reverse


class HomeTest(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('app_home:home'))
        self.assertEqual(response.status_code, 200)

