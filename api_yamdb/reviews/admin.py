from django.contrib import admin

from reviews.models import Titles, Categories, Genres

class TitlesAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'year',
        'description',
        'categories',
        'genres'
    )
    list_editable = ('categories', 'genres')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


admin.site.register(Titles, TitlesAdmin,)
admin.site.register(Categories)
admin.site.register(Genres)
