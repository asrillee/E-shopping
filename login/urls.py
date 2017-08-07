from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.UserLoginView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]