from django.conf.urls import url
from . import views
from .models import Question

urlpatterns = [
    url(r'^tests/(?P<test_id>\d+)/$', views.tests, name='tests'),
    url(r'^$', views.index, name='index'),
    url(r'^result/(?P<res>\d+)/(?P<total>\d+)/$', views.result, name='result'),
]
