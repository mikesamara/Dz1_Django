
from datetime import  timedelta, datetime
from random import random, choice, randint, uniform

from click.core import F
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import logging
from .models import Client1, Product1, Order1, OrderProducts

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

    for i in range(10):
        client = Client1(name=f'name{i}', mail=f'email{i}@mail.ru', number_phone=f'phone +375(29)20{i}-2{i}-{i}2',
                         adress=f'пр-т Дзержинского{i + 1}')
        client.save()
    list_clients = Client1.objects.all()
    return render(request, "myapp/client.html", {'list_clients': list_clients})


def create_product(request):
    logger.info("Заполняем таблицу продуктов")

    for i in range(10):
        product = Product1(name=f'name{i}', description=f'description{i} ge dfg wer wed', price=f'{round(uniform(10.00, 100.00), 2)}',
                         count=f'{randint(1, 10)}')
        product.save()

    list_product = Product1.objects.all()
    return render(request, 'myapp/product.html', {'list_product': list_product})

def create_order(request):
    products = Product1.objects.all()
    clients = Client1.objects.all()
    for client in clients:
        order = Order1(client_order=client, total_price=0)
        for _ in range(randint(1, 5)):
            product = choice(products)
            order.product.add(product)
            total_price = Order1.calculate_total_amount(product.price)
            order.save()
    return HttpResponse(f'{order}')

def order_client(request, client_id):
    client = get_object_or_404(Client1, pk=client_id)
    order_prods = OrderProducts.objects.select_related('product').select_related('order').filter(
        order__client_id=client_id).order_by('-order_id')

    order_prods = order_prods.annotate(prod_cost=F('product__price') * F('product_count'))

    context = {
        'client_name': client.name,
        'orders': order_prods,
    }

    return render(request, 'myapp/client_orders.html', context)

def client_last_orders(request, client_id):
    client = get_object_or_404(Client1, pk=client_id)
    last_week = datetime.now() - timedelta(days=7)
    last_month = datetime.now() - timedelta(days=30)
    last_year = datetime.now() - timedelta(days=365)

    orders_last_week = Order1.objects.filter(client_order=client, date=last_week)
    orders_last_month = Order1.objects.filter(client_order=client, date=last_month)
    orders_last_year = Order1.objects.filter(client_order=client, date=last_year)

    products_last_week = set()
    products_last_month = set()
    products_last_year = set()

    for order in orders_last_week:
        for product in order.products.all():
            products_last_week.add(product)

    for order in orders_last_month:
        for product in order.products.all():
            products_last_month.add(product)

    for order in orders_last_year:
        for product in order.products.all():
            products_last_year.add(product)

    return render(request, 'myapp/client_last_orders.html', {
        'products_last_week': products_last_week,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year
    })





# Create your views here.
