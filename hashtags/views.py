from django.shortcuts import render
from . import models

def all_books(request):
    if request.method == 'GET':
        all_books = models.Product.objects.all()
        context = {'all_books': all_books}
        return render(request, template_name='hashtags/all_books.html', context=context)

def fairy_tales_book(request):
    if request.method == 'GET':
        fairy_tales_book = models.Product.objects.filter(tags__name='Сказки')
        context = {'fairy_tales_book': fairy_tales_book}
        return render(request, template_name='hashtags/fairy_tales_book.html', context=context)

def fantasy_book(request):
    is request.method == 'GET':
    fantasy_book = models.Product.objects.filter(tags__name='Фантастика')
    context = {'fantasy_book': fantasy_book}
    return render(request, template_name='hashtags/fantasy_book.html', context=context)

def drama_book(request):
    if request.method == 'GET':
        drama_book = models.Product.objects.filter(tags__name='Драма')
        context = {'drama_book': drama_book}
        return render(request, template_name='hashtags/drama_book.html', context=context)

