from django.urls import path
from .views import MovieList, MovieDetail,PersonDetail,\
    CreateVote,UpdateVote, MovieImageUpload, TopMovies

app_name = 'core'

urlpatterns = [
    path('', MovieList.as_view(), name='MovieList'),
    path('movies/top', TopMovies.as_view(), name='TopMovies'),
    path('movie/<pk>/', MovieDetail.as_view(), name='MovieDetail'),
    path('movie/<movie_id>/vote', CreateVote.as_view(), name='CreateVote'),
    path('movie/<movie_id>/vote/<pk>', UpdateVote.as_view(), name='UpdateVote'),
    path('person/<pk>/', PersonDetail.as_view(), name='PersonDetail'),
    path('movie/<int:movie_id>/image/upload', MovieImageUpload.as_view(), name='MovieImageUpload'),
]