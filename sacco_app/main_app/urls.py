from django.urls import path
from django.conf.urls import url
from main_app.views import *

app_name = 'main_app'


urlpatterns = [

	url(r'^$',home_view, name = 'index'),
	
]
