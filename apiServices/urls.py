from django.conf.urls import patterns, url
from apiServices import views
urlpatterns = patterns('',
	url(r'^/', views.spotifyQuery, name='spotify'),
  	url(r'^$', views.index, name='index'),
  )