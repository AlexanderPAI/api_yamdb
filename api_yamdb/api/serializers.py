from rest_framework import serializers

from reviews.models import Titles, Categories, Genres

class TitlesSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        read_only=True, slug_field='slug'
    )
    genres = serializers.SlugRelatedField(
        read_only=True, slug_field='slug'
    )
    class Meta:
        fields = '__all__'
        read_only_fields = ('genre', 'categories')
        model = Titles

class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
