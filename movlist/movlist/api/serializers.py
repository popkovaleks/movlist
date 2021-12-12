from rest_framework import serializers

class MoviesSerializer(serializers.Serializer):
    name = serializers.CharField(
        required = True
    )

    director = serializers.CharField(
        required = False,
        default=None
    )

    year = serializers.IntegerField(
        required = False,
        default=None,
        allow_null=True
    )

    is_watched = serializers.BooleanField(
        default=False,
        required=False
    )