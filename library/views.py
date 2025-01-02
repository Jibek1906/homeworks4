from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
                <p><strong>P.S.</strong> И нет, мои сестры не участвовали в 'беременна в 16'. Я просто младший ребенок в семье. Когда я родилась, моей маме было 38 лет, а папе — 45. Любимый ребенок :)</p>
                <img src="https://support.sendible.com/hc/article_attachments/360059727732" alt="Image">
            </body>
        </html>
        """
        return HttpResponse(response_content)

def system_time(request):
    now = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f"Системное время: {now.strftime('%H:%M:%S')}")
