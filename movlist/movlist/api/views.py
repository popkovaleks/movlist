from rest_framework import viewsets, status
from rest_framework.response import Response

from movlist.api import serializers
from movlist.models import Movie

class Movies(viewsets.ViewSet):

    def list(self, request):
        movies = Movie.objects.all()
        
        if movies:
            return Response(data=serializers.MoviesSerializer(movies, many=True).data, status=status.HTTP_200_OK)
        return Response('No film found', status=status.HTTP_404_NOT_FOUND)

    def add(self, request):
        pass