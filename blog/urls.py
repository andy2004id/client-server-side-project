from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/post_football/$', views.post_football, name='post_football'),
	url(r'^search/$', views.search, name='search'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
	url(r'^contact/$', views.contact, name='contact'),


]