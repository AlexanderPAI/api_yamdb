from csv import DictReader
from django.core.management import BaseCommand

# Import the model
from reviews.models import Titles, Categories, Genres, GenresTitles

MODELS = [Titles, Categories, Genres]


class Command(BaseCommand):
    # Show this when the user types help
    for model in MODELS:
        model.objects.all().delete()
    help = "Loads data from children.csv"

    def handle(self, *args, **options):
        # Show this before loading the data into the database
        print("Loading models data")

        for row in DictReader(open('./static/data/category.csv', encoding="utf8")):
            category = Categories(id=row['id'], name=row['name'], slug=row['slug'])
            category.save()

        for row in DictReader(open('./static/data/genre.csv', encoding="utf8")):
            genre = Genres(id=row['id'], name=row['name'], slug=row['slug'])
            genre.save()

        # Code to load the data into database
        for row in DictReader(open('./static/data/titles.csv', encoding="utf8")):
            titles = Titles(id=row['id'], name=row['name'], year=row['year'], category_id=row['category'])
            titles.save()

        for row in DictReader(open('./static/data/genre_title.csv', encoding="utf8")):
            sunc = GenresTitles(id=row['id'],genre=row['genre_id'], title=row['title_id'])
            sunc.save()