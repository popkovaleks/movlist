from django.views.generic import ListView
from django.http import HttpResponse

import json

from movlist.models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movlist/all_movies.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        context['watched_movies'] = Movie.objects.filter(is_watched=True)
        context['not_watched_movies'] = Movie.objects.filter(is_watched=False)
        return context

def change_status(request):
    if request.method == "POST":

        checked = True if request.POST.get('is_watched') == 'true' else False
        
        if checked:
            Movie.check_watched(request.POST.get('id'))
        if not checked:
            Movie.uncheck_watched(request.POST.get('id'))
        return HttpResponse(status=200)

def get_random_movie(request):
    random_movie = Movie.objects.filter(is_watched=False).order_by('?').first()
    movie = {
        "id": random_movie.id,
        "name": random_movie.name,
        "director": random_movie.director,
        "year": random_movie.year,
        "is_watched": random_movie.is_watched
    }
    if random_movie:
        return HttpResponse(json.dumps(movie), content_type='application/json')
    return HttpResponse(status=404)