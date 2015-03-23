from django.conf.urls import patterns, url

from centers.views import CenterList
from centers.views import CenterDetail
from centers.views import reviews

urlpatterns = patterns(
    '',

    url(r'^$', CenterList.as_view(), name='list'),
    url(r'^(?P<slug>\w{5})/$', CenterDetail.as_view(), name='detail'),
    url(r'^(?P<slug>\w{5})/reviews/$', reviews, name='reviews'),
)
