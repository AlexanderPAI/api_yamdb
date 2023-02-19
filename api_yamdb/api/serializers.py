import datetime

from rest_framework import serializers

from reviews.models import Titles, Categories, Genres

from users.models import User
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.decorators import action


class TitlesSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
        required=True
    )
    genres = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        required=True
    )
    year = serializers.IntegerField(
        min_value=0,
        max_value=datetime.date.today().year
    )

    class Meta:
        fields = '__all__'
        model = Titles


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genres


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Categories


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        #validators = [
        #    UniqueTogetherValidator(
        #        queryset=User.objects.all(),
        #        fields=('username', 'email')
        #    )
        #]
