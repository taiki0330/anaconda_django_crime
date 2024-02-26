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

    def get_context_data(self, **kwargs):
        # まず親クラスのget_context_dataを呼び出して、既存のコンテキストを取得する
        context = super().get_context_data(**kwargs)
        # URLから取得したジャンルIDに基づいてジャンル名を取得する
        context['genre_name'] = GenreModel.objects.get(id=self.kwargs['genre_id']).genre_name
        return context

    def get_queryset(self):
        """ジャンルIDに基づいて犯罪リストをフィルタリングする。"""
        return CrimeModel.objects.filter(genre_id=self.kwargs['genre_id']).prefetch_related('suspectmodel_set', 'victimmodel_set')



class CrimeDetail(DetailView):
    model = CrimeModel
    template_name = 'crime_detail.html'

    def get_queryset(self):
        """関連する容疑者と被害者の情報も取得する。"""
        return CrimeModel.objects.prefetch_related('suspectmodel_set', 'victimmodel_set')


class SuspectDetail(DetailView):
    model = SuspectModel
    template_name = 'suspect_detail.html'

class VictimDetail(DetailView):
    model = VictimModel
    template_name = 'victim_detail.html'