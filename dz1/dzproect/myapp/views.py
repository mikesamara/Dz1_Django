import random

from django.http import HttpResponse
from django.shortcuts import render
import logging
from .models import Client1, Product1, Order1

# -*- coding: utf-8 -*-

logger = logging.getLogger(__name__)


def index(request):
    logger.info(" Перешли на главную страницу ")
    return HttpResponse("<h1>Добро пожаловать на мой первый Django сайт!</h1>")


def about(request):
    logger.info("Перешли на страницу обо мне ")
    return HttpResponse("</br><p>Меня зовут Михаил и я начинающий Django разработчик.</p>"
                        "<p>На этом сайте я планирую делиться своими проектами, уроками и опытом в области веб-разработки.</p>")


def create_client(request):
    logger.info("Заполняем таблицу клиентов")
    res = []
    for i in range(10):
        client = Client1(name=f'name{i}', mail=f'email{i}@mail.ru', number_phone=f'phone +375(29)20{i}-2{i}-{i}2',
                         adress=f'пр-т Дзержинского{i + 1}')
        client.save()
        res.append(client.name_client())
    return HttpResponse(f"{res}")


def create_product(request):
    logger.info("Заполняем таблицу продуктов")
    res = []
    for i in range(10):
        product = Product1(name=f'name{i}', description=f'description{i} ge dfg wer wed', price=f'{round(random.uniform(10.00, 100.00), 2)}',
                         count=f'{random.randint(1, 10)}')
        product.save()
        res.append(product.products_list())
    return HttpResponse(f"{res}")

def create_order(client, products, total_amount):
    order = Order1(client_order=client, total_price=total_amount)
    order.save()
    order.product.add(*products)
    return HttpResponse (f'{order}')


# Create your views here.
