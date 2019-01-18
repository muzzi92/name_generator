from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'entry/$', views.entry, name='entry'),
    url(r'select/$', views.select, name='select'),
    url(r'create/$', views.create, name='create'),
]
