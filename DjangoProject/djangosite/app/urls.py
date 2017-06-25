from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'register',views.register),
    url(r'post_list',views.post_list),
    url(r'moments_input', views.moments_input),
    url(r'',views.welcome),
]