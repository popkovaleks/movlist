"""movlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from movlist.views import change_status, get_random_movie
from movlist.views import MovieListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movlist.api.urls')),
    path('', MovieListView.as_view()),
    path('change_status/', change_status, name="change_status"),
    path('get-random-movie/', get_random_movie, name="get_random_movie")
]
