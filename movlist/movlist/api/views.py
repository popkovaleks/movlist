from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from movlist.api import serializers
from movlist.models import Movie

class Movies(viewsets.ViewSet):

    def list(self, request):
        print(isinstance(self.request.query_params.get('is_watched'), bool))

        movies = Movie.objects.all()
        
        if movies:
            return Response(data=serializers.MoviesSerializer(movies, many=True).data, status=status.HTTP_200_OK)
        return Response('No movie found', status=status.HTTP_404_NOT_FOUND)

    def add(self, request):
        
        data = request.data
        serializer = serializers.MoviesSerializer(data=data)
        
        if serializer.is_valid():
            Movie.objects.create(
                name=serializer.data['name'],
                director=serializer.data['director'],
                year=serializer.data['year'],
                is_watched=serializer.data['is_watched']
                )
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def change_status(self, request):
        pass