from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import GenresViewSet, TitlesViewSet, CategoriesViewSet, UserViewSet

router = DefaultRouter()

router.register('genres', GenresViewSet, basename='genres')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('titles', TitlesViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
]