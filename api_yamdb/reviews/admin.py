from django.contrib import admin

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title


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


admin.site.register(Title, TitlesAdmin,)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(Genre, GenresAdmin)
admin.site.register(GenreTitle, GenresTitlesAdmin)
admin.site.register(Review)
admin.site.register(Comment)
