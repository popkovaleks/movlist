from django.contrib import admin

from movlist.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('name', 'director', 'year', 'watched')