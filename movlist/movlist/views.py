from django.views.generic import ListView
from django.http import HttpResponse

from movlist.models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movlist/all_movies.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.all()


def change_status(request):
    if request.method == "POST":

        checked = True if request.POST.get('is_watched') == 'true' else False
        
        if checked:
            Movie.check_watched(request.POST.get('id'))
        if not checked:
            Movie.uncheck_watched(request.POST.get('id'))
        return HttpResponse(status=200)