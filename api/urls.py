from django.contrib import admin
from django.urls import include, path, re_path
from api import views

from django.views.generic import TemplateView

app_name = 'api'


urlpatterns = [
    # retrive/update/delete APIs
    path('post-detail/<int:pk>/', views.PostDetailAPI.as_view(),name="post-detail"),
    path('post-list-create/', views.PostListAPI.as_view(),name="post-list"),
]