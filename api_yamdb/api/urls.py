from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import GenresViewSet, TitlesViewSet, CategoriesViewSet, UserViewSet

router = DefaultRouter()

router.register(r'genres', GenresViewSet, basename='genres')
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'titles', TitlesViewSet, basename='titles')
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
]