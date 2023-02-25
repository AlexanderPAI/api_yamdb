from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       GetTokenView, ReviewViewSet, SignUpViewSet,
                       TitleViewSet, UserViewSet)

router = DefaultRouter()

router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')
router.register('auth/signup', SignUpViewSet, basename='signup')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', GetTokenView.as_view(), name='get_token'),
]
