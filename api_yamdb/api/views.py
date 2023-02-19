from rest_framework import viewsets, mixins
from rest_framework.filters import  SearchFilter

from api.permissions import IsAdminPermission # IsAdminOrReadOnly
from api.serializers import GenresSerializer, CategoriesSerializer, TitlesSerializer, UserSerializer
from reviews.models import Genres, Titles, Categories
from users.models import User


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


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
