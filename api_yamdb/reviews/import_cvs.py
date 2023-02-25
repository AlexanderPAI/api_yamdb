# path: venv/Lib/site-packages/django/core/management/commands/import_cvs.py
# for start print: python manage.py import_cvs
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

MODELS = [Title, Category, Genre, Review, GenreTitle, Comment, User]


class Command(BaseCommand):
    for model in MODELS:
        model.objects.all().delete()

    def handle(self, *args, **options):
        # Show this before loading the data into the database
        print("Loading models data")

        for row in DictReader(
            open('./static/data/category.csv', encoding="utf8")
        ):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            category.save()

        for row in DictReader(
            open('./static/data/genre.csv', encoding="utf8")
        ):
            genre = Genre(id=row['id'], name=row['name'], slug=row['slug'])
            genre.save()

        # Code to load the data into database
        for row in DictReader(
            open('./static/data/titles.csv', encoding="utf8")
        ):
            titles = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category']
            )
            titles.save()

        for row in DictReader(
            open('./static/data/genre_title.csv', encoding="utf8")
        ):
            sunc = GenreTitle(
                id=row['id'], genre=row['genre_id'], title=row['title_id']
            )
            sunc.save()
