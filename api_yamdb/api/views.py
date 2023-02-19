from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Comment, Review
from .serializers_2 import CommentSerializer, ReviewSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Представление модели комменатриев."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class ReviewViewSet(viewsets.ModelViewSet):
    """Представление модели отзывов"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    # permission_classes = (IsAdminOrReadOnly,)
