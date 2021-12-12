from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.renderers import JSONRenderer

from movlist.api import serializers
from movlist.models import Movie

class Movies(viewsets.ViewSet):

    def list(self, request):
        is_watched = self.request.query_params.get('is_watched')
        movies = Movie.objects.all() if is_watched == None else Movie.objects.filter(is_watched=is_watched)
        
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

        data = request.data
        #movie = Movie.objects.get(name=request.data['name'])
        serializer = serializers.MoviesSerializer(data=data)
        if serializer.is_valid():
            Movie.objects.filter(name=request.data['name']).update(
                is_watched=request.data['is_watched']
            )
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class GetRandomMovie(viewsets.ViewSet):
    def get_random_movie(self,request):
        random_movie = Movie.objects.filter(is_watched=False).order_by('?').first()
        movie = {
            "name": random_movie.name,
            "director": random_movie.director,
            "year": random_movie.year,
            "is_watched": random_movie.is_watched
        }
        if random_movie:
            return Response(data=movie, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)