from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import GenresViewSet

router = DefaultRouter()

router.register('genres', GenresViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
]