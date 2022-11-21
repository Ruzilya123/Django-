from django.http import HttpResponse

# Create your views here.

def index(request, fio, age, int):
    return HttpResponse(f"""<h2>Главная</h2>
    <p>ФИО: {fio}</p>
    <p>Возраст: {age}</p>
    <p>Интересы: {int}</p>""")

def about(request, pr, us, love):
    return HttpResponse(f"""<h2>О Пользователе</h2>
    <p>Откуда приехала: {pr}</p>
    <p>Успеваемость в школе: {us}</p>
    <p>Любите/не любите учиться: {love}</p>""")

def contact(request, Telegram, VK, gitlab):
    return HttpResponse(f"""<h2>Контакты</h2>
    <a href="https://t.me/Ruzya0_0" target="_blank">{Telegram}</a>
    <a href="https://vk.com/ruzilya142006" target="_blank">{VK}</a>
    <a href="https://gitlab.com/salimovaruzila02" target="_blank">{gitlab}</a>""")
