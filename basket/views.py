from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

def create_order_view(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('orders_list')
    else:
        form = forms.BasketForm()
    return render(request, template_name='basket/create_order.html', context={'form': form})

def orders_list_view(request):
    if request.method == 'GET':
        orders_list = models.BasketModel.objects.all().order_by('-id')
        context = {'orders_list': orders_list}
        return render(request, template_name='basket/orders_list.html', context=context)

def order_detail_view(request, id):
    if request.method == 'GET':
        order_id = get_object_or_404(models.BasketModel, id=id)
        context = {'order_id': order_id}
        return render(request, template_name='basket/order_detail.html', context=context)

def order_update_view(request, id):
    order_id = get_object_or_404(models.BasketModel, id=id)
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES, instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('orders_list')
    else:
        form = forms.BasketForm(instance=order_id)
    return render(request, template_name='basket/order_update.html', context={'form': form, 'id': id})
    
def order_delete_view(request, id):
    order_id = get_object_or_404(models.BasketModel, id=id)
    order_id.delete()
    return redirect('orders_list')

