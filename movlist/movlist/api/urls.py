from django.urls import path

from movlist.api import views

urlpatterns = [
    path('movies/', views.Movies.as_view(
        {
            'get': 'list',
            'post': 'add',
            'put': 'change_status'
        }
    )),
    path('get-random-movie/', views.GetRandomMovie.as_view(
        {
            'get': 'get_random_movie'
        }
    ))
]