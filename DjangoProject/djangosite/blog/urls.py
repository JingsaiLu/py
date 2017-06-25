from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'blog_index', views.blog_index),
]