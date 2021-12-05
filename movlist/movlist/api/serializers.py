from rest_framework import serializers

class MoviesSerializer(serializers.Serializer):
    name = serializers.CharField(
        required = True
    )

    director = serializers.CharField(
        required = False
    )

    year = serializers.IntegerField(
        required = False
    )

    is_wathched = serializers.BooleanField(
        default=False,
        required=False
    )