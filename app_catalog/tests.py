from django.test import TestCase
from django.urls import reverse

from app_catalog.models import Item


class TestAppCatalog(TestCase):

    fixtures = ['fixtures/catalog.json']
    def test_catalog(self):
        response = self.client.get(reverse('app_catalog:catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Каталог')
        self.assertEqual(response.context['title'], 'Каталог')
        self.assertTemplateUsed(response, 'app_catalog/catalog.html')


    def test_category_detail(self):
        response = self.client.get(reverse('app_catalog:category_detail', args=['picca']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Пицца')
        self.assertEqual(response.context['title'], 'Пицца')
        self.assertTemplateUsed(response, 'app_catalog/catalog.html')

    def test_item_card(self):
        item = Item.objects.get(id=1)
        response = self.client.get(reverse('app_catalog:item_detail_view', args=[item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, item.name)
        self.assertEqual(response.context['title'], item.name)
        self.assertTemplateUsed(response, 'app_catalog/card.html')