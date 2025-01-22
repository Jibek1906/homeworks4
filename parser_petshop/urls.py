from django.urls import path
from . import views

urlpatterns = [
    path('petshop_list/', views.PetShopListView.as_view(), name='petshop_list'),
    path('petshop_form/', views.PetShopFormView.as_view(), name='petshop_form'),
]