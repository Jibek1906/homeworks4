from django.shortcuts import render
from django.http import HttpResponse
from . import models, forms
from django.views import generic

class PetShopListView(generic.ListView):
    template_name = 'parser/petshop_list.html'
    context_object_name = 'petshop_list'
    model = models.PetShopModel

    def get_queryset(self):
        return self.model.objects.all()

class PetShopFormView(generic.FormView):
    template_name = 'parser/petshop_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            form.parser_data()
            return HttpResponse('Парсер прошел успешно')
        else:
            super(PetShopFormView, self).post(request, *args, **kwargs)
