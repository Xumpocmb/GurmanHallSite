"""GurmanHallSite URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')),
    path('catalog/', include('app_catalog.urls')),
    path('user/', include('app_user.urls')),
    path('order/', include('app_order.urls')),
    path('carts/', include('app_cart.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += path("__debug__/", include("debug_toolbar.urls")),
