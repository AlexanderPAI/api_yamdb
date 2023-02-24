from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.permissions import (IsAccessEditPermission, IsAdminOrReadOnly,
                             IsAdminPermission)
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleForReadSerializer, TitleSerializer,
                             UserSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from reviews.models import Category, Genre, Review, Title
from users.models import User


class GetPostDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class GenreViewSet(GetPostDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class CategoryViewSet(GetPostDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)

    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('name', 'year', 'description')

    def get_queryset(self):
        queryset = Title.objects.all()
        genre = self.request.query_params.get('genre')
        category = self.request.query_params.get('category')
        if genre is not None:
            queryset = queryset.filter(genre__slug=genre)
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleForReadSerializer
        return TitleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    permission_classes = (IsAdminPermission,)
    lookup_field = 'username'  # заменить в эндпоинте id на username
    filter_backends = (SearchFilter, )
    search_fields = ('username',)

    # Нестандартное действие - для этого пишется метод
    # и оборачивается в декоратор @action
    # URL эндпоинта = <префикс>/<название_метода>
    @action(
        methods=(['get', 'patch']),
        detail=False,
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        # перед serilizer.save всегда должен быть serializer.is_valid
        serializer.save(role=request.user.role)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAccessEditPermission,)

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
    permission_classes = (IsAccessEditPermission,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        new_queryset = Review.objects.filter(title=title_id)
        return new_queryset

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        serializer.save(
            author=self.request.user, title=title
        )
