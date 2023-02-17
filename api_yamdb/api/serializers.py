import datetime

from rest_framework import serializers

from reviews.models import Titles, Categories, Genres, GenresTitles


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genres
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Categories
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreTitleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True,
        many=True
    )

    class Meta:
        model = Genres
        fields = ('slug',)


class TitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
        required=True
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
        required=True,
        many=True
    )
    year = serializers.IntegerField(
        min_value=0,
        max_value=datetime.date.today().year
    )

    class Meta:
        fields = '__all__'
        model = Titles
