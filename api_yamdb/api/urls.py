from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoriesViewSet, GenresViewSet, TitlesViewSet,
                       UserViewSet, ReviewViewSet, CommentViewSet)

router = DefaultRouter()

router.register('genres',GenresViewSet, basename='genres')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('titles', TitlesViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='reviews'
                )
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewSet,
                basename='comments'
                )

urlpatterns = [
    path('', include(router.urls)),
]
