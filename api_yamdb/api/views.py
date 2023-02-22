from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (DjangoModelPermissionsOrAnonReadOnly,
                                        IsAdminUser, IsAuthenticated)
from rest_framework.response import Response

from api.permissions import IsAdminOrReadOnly, IsAdminPermission
from api.serializers import (CategoriesSerializer, GenresSerializer,
                             GenreTitleSerializer, TitlesSerializer,
                             UserSerializer, CommentSerializer, ReviewSerializer)
from reviews.models import Categories, Genres, Titles, Comment, Review
from users.models import User


class GetPostDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class GenresViewSet(GetPostDeleteViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    # permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class CategoriesViewSet(GetPostDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    # permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    # permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('genre', 'category', 'year', 'name')

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    permission_classes = (IsAdminPermission,)
    lookup_field = 'username'
    filter_backends = (SearchFilter, )
    search_fields = ('username',)

    # Нестандартное действие - для этого пишется метод 
    # и оборачивается в декоратор @action
    # URL эндпоинта = <префикс>/<название_метода>
    @action(
        methods=(['get', 'patch']),
        detail=False,
        permission_classes = (IsAuthenticated,)
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # перед serilizer.save всегда должен быть serializer.is_valid
        serializer.save(role=request.user.role)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = (AdminModeratorAuthorPermission,)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # permission_classes = (AdminModeratorAuthorPermission,)

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
