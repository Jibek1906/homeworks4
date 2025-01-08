from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

#Список книг
def books_list(request):
    if request.method == 'GET':
        books_list = models.Books.objects.all().order_by('-id')
        context = {'books_list': books_list}
        return render(request, template_name='book.html', context=context)

def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)















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
