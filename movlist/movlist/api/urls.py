from django.urls import path

from movlist.api import views

urlpatterns = [
    path('movies/', views.Movies.as_view(
        {
            'get': 'list'
        }
    ))
]