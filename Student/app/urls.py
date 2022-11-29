from django.urls import path
from .views import test_get, test_post

urlpatterns = [
    path('', test_get),
    path('post/', test_post),
]