from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me, name='about me'),
    path('about_my_pets/', views.about_my_pets, name='about my pets'),
    path('date_time/', views.date_time, name='date time'),
]