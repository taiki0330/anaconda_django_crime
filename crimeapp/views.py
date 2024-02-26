from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import GenreModel, CrimeModel, SuspectModel, VictimModel

# Create your views here.
class GenreList(ListView):
    model = GenreModel
    template_name = 'genre_list.html'

class CrimeList(ListView):
    model = CrimeModel
    template_name = 'crime_list.html'

class CrimeDetail(DetailView):
    model = CrimeModel
    template_name = 'crime_detail.html'

class SuspectDetail(DetailView):
    model = SuspectModel
    template_name = 'suspect_detail.html'

class VictimDetail(DetailView):
    model = VictimModel
    template_name = 'victim_detail.html'