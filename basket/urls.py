from django.urls import path
from . import views

urlpatterns = [
    path('create_order/', views.create_order_view, name='create_order'),
    path('orders_list/', views.orders_list_view, name='orders_list'),
    path('orders_list/<int:id>/', views.order_detail_view, name='order_detail'),
    path('orders_list/<int:id>/update/', views.order_update_view, name='order_update'),
    path('orders_list/<int:id>/delete/', views.order_delete_view, name='order_delete'),
]