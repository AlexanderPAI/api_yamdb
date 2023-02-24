from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                       UserViewSet)

router = DefaultRouter()

router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')
# роутер для reviews
# роутер для comments

urlpatterns = [
    path('', include(router.urls)),
]