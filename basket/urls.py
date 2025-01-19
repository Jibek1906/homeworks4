from django.urls import path
from . import views

urlpatterns = [
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
    path('orders_list/', views.OrdersListView.as_view(), name='orders_list'),
    path('orders_list/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders_list/<int:id>/update/', views.UpdateOrderView.as_view(), name='order_update'),
    path('orders_list/<int:id>/delete/', views.DeleteOrderView.as_view(), name='order_delete'),
]