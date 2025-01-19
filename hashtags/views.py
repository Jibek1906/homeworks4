from django.shortcuts import render
from . import models
from django.views import generic

class AllBooksView(generic.ListView):
    template_name = 'hashtags/all_books.html'
    context_object_name = 'all_books'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.all()

class FairyTalesBooksView(generic.ListView):
    template_name = 'hashtags/fairy_tales_books.html'
    context_object_name = 'fairy_tales_books'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Сказки')

class FantasyBooksView(generic.ListView):
    template_name = 'hashtags/fantasy_books.html'
    context_object_name = 'fantasy_books'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Фантастика')

class DramaBooksView(generic.ListView):
    template_name = 'hashtags/drama_books.html'
    context_object_name = 'drama_books'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Драма')