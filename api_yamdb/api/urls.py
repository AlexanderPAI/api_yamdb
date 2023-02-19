from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoriesViewSet, GenresViewSet, TitlesViewSet,
                       UserViewSet)

router = DefaultRouter()

router.register('genres', GenresViewSet, basename='genres')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('titles', TitlesViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')
# роутер для reviews
# роутер для comments

urlpatterns = [
    path('', include(router.urls)),
]