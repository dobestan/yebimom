from django.conf.urls import patterns, url

# Views
from api.views.events import EventList, EventDetail
from api.views.centers import CenterList, CenterDetail
from api.views.regions import RegionList
from api.views.reviews import UserReviewList


urlpatterns = patterns(
    '',

    url(r'^login/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^events/$', EventList.as_view(), name='events-list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='events-detail'),

    url(r'^centers/$', CenterList.as_view(), name='centers-list'),
    url(r'^centers/(?P<hash_id>\w{5})/$', CenterDetail.as_view(), name='centers-detail'),

    url(r'^regions/$', RegionList.as_view(), name='regions-list'),

    url(r'^reviews/$', UserReviewList.as_view(), name='reviews-list'),
)
