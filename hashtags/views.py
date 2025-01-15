from django.shortcuts import render
from . import models

def all_books_view(request):
    if request.method == 'GET':
        all_books = models.Product.objects.all()
        context = {'all_books': all_books}
        return render(request, template_name='hashtags/all_books.html', context=context)

def fairy_tales_books_view(request):
    if request.method == 'GET':
        fairy_tales_books = models.Product.objects.filter(tags__name='Сказки')
        context = {'fairy_tales_books': fairy_tales_books}
        return render(request, template_name='hashtags/fairy_tales_books.html', context=context)

def fantasy_books_view(request):
    if request.method == 'GET':
        fantasy_books = models.Product.objects.filter(tags__name='Фантастика')
        context = {'fantasy_books': fantasy_books}
        return render(request, template_name='hashtags/fantasy_books.html', context=context)

def drama_books_view(request):
    if request.method == 'GET':
        drama_books = models.Product.objects.filter(tags__name='Драма')
        context = {'drama_books': drama_books}
        return render(request, template_name='hashtags/drama_books.html', context=context)

