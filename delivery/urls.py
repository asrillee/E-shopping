from django.conf.urls import url
from . import views

app_name = 'delivery'

urlpatterns = [
    url(r'^$', views.home, name='delivery'),
]