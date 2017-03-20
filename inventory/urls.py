from django.conf.urls import url

from . import views

app_name = 'inventory'
urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),


]