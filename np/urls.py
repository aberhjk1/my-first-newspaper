from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/$', views.post_new, name='post_new'),
    url(r'^section/(?P<section>[\w-]+)/$', views.section_filtered, name='section_filtered'),
    url(r'^article/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^article/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),


]