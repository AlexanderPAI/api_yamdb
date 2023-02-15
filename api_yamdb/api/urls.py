from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import GenresViewSet, TitlesViewSet, CategoriesViewSet

router = DefaultRouter()

router.register('genres', GenresViewSet, basename='genre')
router.register('categories', CategoriesViewSet, basename='category')
router.register('titles', TitlesViewSet, basename='title')

urlpatterns = [
    path('', include(router.urls)),
]