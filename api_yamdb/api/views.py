from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter

from api.serializers import GenresSerializer, CategoriesSerializer, TitlesSerializer
from reviews.models import Genres, Titles, Categories


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,)
    pagination_class = None
    search_fields = ('genres', 'categories', 'year', 'name')
