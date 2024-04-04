from django.http import HttpResponse
from django.shortcuts import render
import logging
# -*- coding: utf-8 -*-

logger = logging.getLogger(__name__)



def index(request):
    logger.info(" Перешли на главную страницу ")
    return HttpResponse("<h1>Добро пожаловать на мой первый Django сайт!</h1>")


def about(request):
    logger.info("Перешли на страницу обо мне ")
    return HttpResponse("</br><p>Меня зовут Михаил и я начинающий Django разработчик.</p>"
                        "<p>На этом сайте я планирую делиться своими проектами, уроками и опытом в области веб-разработки.</p>")

# Create your views here.
