from django.urls import path
from .views import GenreList, CrimeList, CrimeDetail, SuspectDetail, VictimDetail
urlpatterns = [
    path('genre/', GenreList.as_view(), name='genre'),
    path('crime/<int:genre_id>/crime/', CrimeList.as_view(), name='crime'),
    path('crime/<int:pk>/', CrimeDetail.as_view(), name='crime_detail'),
    path('suspect/<int:pk>/', SuspectDetail.as_view(), name='suspect'),
    path('victim/<int:pk>/', VictimDetail.as_view(), name='victim')
]