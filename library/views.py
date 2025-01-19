from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models, forms
from django.views import generic
from django.urls import reverse

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books_list'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

#Список книг
class BooksListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books_list'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)

class CreateReviewView(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.ReviewForm

    def get_success_url(self):
        return reverse('book_detail', kwargs={'id': self.object.reviews_choice.id})

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)
















def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Жибек, я ученица университета Ала-Тоо и в этом году уже буду писать дипломную работу. До этого окончила колледж при этом же университете. Хорошо владею русским и английским языками, но кыргызский знаю слабо, так как училась в школе с русским уклоном. Моё хобби — смотреть аниме и читать мангу.')

def about_my_pets(request):
    if request.method == 'GET':
        response_content = """
        <html>
            <head>
                <title>О моих питомцах</title>
            </head>
            <body>
                <h1>О домашних животных</h1>
                <p>Домашних животных в нашей семье нет, потому что никто из старших их особо не любит. Зато у меня есть четыре племянника, которые по уровню хаоса и проблем дома ничем не уступают питомцам. Тетей я стала уже в семь лет — настоящий ветеран 'тетских войн'!</p>
                <p>Старшему племяннику 13 лет, средним по 7, а младшему 4. Плюс куча двоюродных племяшек. <strong>Experience 100+</strong>, правда не всегда желанный. Зато недавно за пройденный опыт вручили новый телефон (это того не стоило).</p>
                <p><strong>P.S.</strong> И нет, мои сестры не участвовали в 'беременна в 16'. Я просто поздний и младший ребенок в семье. Когда я родилась, моей маме было 38 лет, а папе — 45. Любимый ребенок :)</p>
                <img src="https://support.sendible.com/hc/article_attachments/360059727732" alt="Image">
            </body>
        </html>
        """
        return HttpResponse(response_content)

def date_time(request):
    now = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f"Системное время: {now.strftime('%H:%M:%S')}")
