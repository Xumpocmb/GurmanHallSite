from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from app_catalog.models import Category, Item


class StaticViewSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return ['app_home:home', 'app_catalog:catalog', 'app_user:profile']

    def location(self, item):
        return reverse(item)

    def changefreq(self, obj):
        return 'weekly'
