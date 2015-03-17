from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from yebimom.sitemaps import sitemaps


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', include('robots.urls')),

    # Django 3rd Party Modules
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Yebimom Urls
    url(r'^$', 'yebimom.views.home', name='home'),

    # Centers Urls
    url(r'^', include('centers.urls')),

    # Included Apps Urls
    url(r'^events/', include('events.urls', namespace='events', app_name='events')),
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
