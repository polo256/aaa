from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'secretariat'

admin.site.site_header = 'Africa Agribusiness Academy'
urlpatterns = [
	
	#url(r'^$', views.index, name='index'),
	url(r'^event/', views.index, name='index'),
	url(r'^event/(?P<id>\d+)/', views.event_detail, name='event_detail'),


]