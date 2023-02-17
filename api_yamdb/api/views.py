from rest_framework import viewsets, mixins
from rest_framework.filters import  SearchFilter

from api.permissions import IsAdminPermission # IsAdminOrReadOnly
from api.serializers import GenresSerializer, CategoriesSerializer, TitlesSerializer, UserSerializer
from reviews.models import Genres, Titles, Categories
from users.models import User


from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

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
    #permission_classes = (IsAdminOrReadOnly,)


class CategoriesViewSet(GetPostDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    #permission_classes = (IsAdminOrReadOnly,)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    #permission_classes = (IsAdminOrReadOnly,)
    #filter_backends = (SearchFilter,)
    pagination_class = None
    search_fields = ('genres', 'categories', 'year', 'name')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminPermission,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('username',)

    #def get_permissions(self):
    #    if self.action == 'list':
    #        return (IsAdminUser(),)
    #    return super().get_permissions()
