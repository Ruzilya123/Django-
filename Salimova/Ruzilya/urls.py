
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, kwargs={"fio":"Салимова Рузиля Азатовна", "age":"16", "int":"Шашки, шахматы, лёгкая атлетика, спортивные игры, программирование"}),
    path('about', views.about, kwargs={"pr":"Республика Башкортостан город Ишимбай улица Калинина дом 49", "us":"Нормальное", "love":"люблю"}),
    path('contact', views.contact, kwargs={"Telegram":"Телеграм", "VK":"Вконтакте", "gitlab":"Гитлаб"}),
]
