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
        null=True
    )

    watched = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name