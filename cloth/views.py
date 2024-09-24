from django.shortcuts import render
from . import models
from django.views import generic

# Create your views here.
class ClothListView(generic.ListView):
    model = models.Cloth
    template_name = 'cloth/cloth_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kids_cloth'] = models.Cloth.objects.filter(tags__name='For Kids')
        context['adults_cloth'] = models.Cloth.objects.filter(tags__name='For Adults')
        context['pensioners_cloth'] = models.Cloth.objects.filter(tags__name='For Pensioners')
        return context