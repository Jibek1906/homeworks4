from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create_review/', views.CreateReviewView.as_view(), name='create_review'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pets/', views.about_my_pets, name='about_my_pets'),
    path('date_time/', views.date_time, name='date_time'),
    path('search/', views.SearchView.as_view(), name='search'),
]