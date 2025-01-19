from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

class CreateOrderView(generic.CreateView):
    template_name = 'basket/create_order.html'
    form_class = forms.BasketForm
    success_url = '/orders_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)

class OrdersListView(generic.ListView):
    template_name = 'basket/orders_list.html'
    context_object_name = 'orders_list'
    model = models.BasketModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class OrderDetailView(generic.DetailView):
    template_name = 'basket/order_detail.html'
    context_object_name = 'order_id'
    model = models.BasketModel

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