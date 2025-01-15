from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books_view, name='all_books'),
    path('fairy_tales_books/', views.fairy_tales_books_view, name='fairy_tales_books'),
    path('fantasy_books/', views.fantasy_books_view, name='fantasy_books'),
    path('drama_books/', views.drama_books_view, name='drama_books'),
]