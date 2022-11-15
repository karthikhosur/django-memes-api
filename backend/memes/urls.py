from django.urls import include, re_path
from django.urls import path, include
from .views import (
    post_collection,
)

urlpatterns = [
    re_path('api', post_collection),
]