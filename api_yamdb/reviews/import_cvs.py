# path: venv/Lib/site-packages/django/core/management/commands/import_cvs.py
from csv import DictReader

from django.core.management import BaseCommand

# Import the model
from users.models import User
from reviews.models import (
    Category,
    Genre,
    Review,
    Title,
    GenreTitle,
    Comment
)

MODELS = [Title, Category, Genre, Review, GenreTitle, Comment, ]


class Command(BaseCommand):
    for model in MODELS:
        model.objects.all().delete()

    def handle(self, *args, **options):
        # Show this before loading the data into the database
        print("Loading models data")

        for row in DictReader(open('./static/data/category.csv', encoding="utf8")):
            category = Category(id=row['id'], name=row['name'], slug=row['slug'])
            category.save()

        for row in DictReader(open('./static/data/genre.csv', encoding="utf8")):
            genre = Genre(id=row['id'], name=row['name'], slug=row['slug'])
            genre.save()

        # Code to load the data into database
        for row in DictReader(open('./static/data/titles.csv', encoding="utf8")):
            titles = Title(id=row['id'], name=row['name'], year=row['year'], category_id=row['category'])
            titles.save()

        for row in DictReader(open('./static/data/genre_title.csv', encoding="utf8")):
            genre_name = Genre.objects.get(pk=row['genre_id'])
            title_name = Title.objects.get(pk=row['title_id'])
            sunc = GenreTitle(id=row['id'], genre=genre_name, title=title_name)
            sunc.save()

        for row in DictReader(open('./static/data/users.csv', encoding="utf8")):
            user = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
            )
            user.save()

        for row in DictReader(open('./static/data/review.csv', encoding="utf8")):
            user_name = User.objects.get(id=row['author'])
            title_name = Title.objects.get(pk=row['title_id'])
            review = Review(id=row['id'],
                            author=user_name,
                            title=title_name,
                            text=row['text'],
                            score=row['score'],
                            pub_date=row['pub_date']
                            )
            review.save()

        for row in DictReader(open('./static/data/comments.csv', encoding="utf8")):
            user_name = User.objects.get(id=row['author'])
            review_id = Review.objects.get(pk=row['review_id'])
            review = Comment(id=row['id'],
                             review=review_id,
                             author=user_name,
                             text=row['text'],
                             pub_date=row['pub_date']
                             )
            review.save()
