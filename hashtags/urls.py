from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.AllBooksView.as_view(), name='all_books'),
    path('fairy_tales_books/', views.FairyTalesBooksView.as_view(), name='fairy_tales_books'),
    path('fantasy_books/', views.FantasyBooksView.as_view(), name='fantasy_books'),
    path('drama_books/', views.DramaBooksView.as_view(), name='drama_books'),
]