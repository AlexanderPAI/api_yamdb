from django.contrib import admin

from reviews.models import Categories, Genres, GenresTitles, Titles


class TitlesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'year',
        'description',
        'category',
    )
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


class CategoriesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'slug'
    )


class GenresAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug'
    )


class GenresTitlesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'genre',
        'title'
    )


admin.site.register(Titles, TitlesAdmin,)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(GenresTitles, GenresTitlesAdmin)
