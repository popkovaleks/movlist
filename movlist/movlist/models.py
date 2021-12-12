from django.db import models


class Movie(models.Model):

    name = models.CharField(
        max_length=500
    )

    director = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    year = models.IntegerField(
        null=True,
        blank=True
    )

    is_watched = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

    def create(self, name, director=None, year=None, is_watched=False):
        self.objects.create(
            name=name,
            director=director,
            year=year,
            is_watched=is_watched
        )
