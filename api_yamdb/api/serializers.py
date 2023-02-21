import datetime

from rest_framework import serializers

from reviews.models import (Categories, Comment, Genres, GenresTitles, Review,
                            Titles)

from rest_framework.decorators import action
from rest_framework.validators import UniqueTogetherValidator

from users.models import User


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
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()

    class Meta:
        model = Genres
        fields = '__all__'


#class CategoryField(serializers.RelatedField):
#    def to_representation(self, value):
#        return value


class TitlesSerializer(serializers.ModelSerializer):
    #category = CategoriesSerializer()
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
        required=True
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
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
    
    #def create(self, validated_data):
    #    category = validated_data.pop('category')
    #    title = Titles.objects.create(**validated_data)
    #    current_category, status = Categories.objects.get_or_create(**category)
    #    Titles.objects.create(title=title, **current_category)
    #    return title


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username', 'email')
            )
        ]


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзывов."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Review
        read_only_fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('id', 'text', 'author', 'pub_date')
