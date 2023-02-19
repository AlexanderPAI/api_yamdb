from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly

from api.permissions import IsAdminOrReadOnly
from api.serializers import GenresSerializer, CategoriesSerializer, TitlesSerializer, GenreTitleSerializer
from reviews.models import Genres, Titles, Categories


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
