from django.urls import include, re_path
from django.urls import path, include
from .views import (
    post_collection,
    cached_post_collection,
    user_subscribe, subscribe_or_not, all_subscribers
)

urlpatterns = [
    re_path('api', post_collection),
    re_path('cache', cached_post_collection),
    re_path('subscribe', user_subscribe),
    re_path('check', subscribe_or_not),
    re_path('all', all_subscribers)
]
