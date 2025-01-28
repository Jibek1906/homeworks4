from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

class CreateOrderView(generic.CreateView):
    template_name = 'basket/create_order.html'
    form_class = forms.BasketForm
    success_url = '/orders_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)

@method_decorator(cache_page(60*20), name='dispatch')
class OrdersListView(generic.ListView):
    template_name = 'basket/orders_list.html'
    context_object_name = 'orders_list'
    model = models.BasketModel

    def get_queryset(self):
        orders = cache.get('orders')
        if not orders:
            orders = self.model.objects.all().order_by('-id')
            cache.set('orders', orders, 60*20)
        return orders

class OrderDetailView(generic.DetailView):
    template_name = 'basket/order_detail.html'
    context_object_name = 'order_id'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=order_id)

class UpdateOrderView(generic.UpdateView):
    template_name = 'basket/order_update.html'
    form_class = forms.BasketForm
    success_url = '/orders_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=order_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)

class DeleteOrderView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/orders_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=order_id)