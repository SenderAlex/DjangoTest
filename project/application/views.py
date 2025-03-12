from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Добро пожаловать в Django</h1>")


def data(request):
    return HttpResponse("<h1>Вы зашли на страницу Django Data</h1>")


def test(request):
    return HttpResponse("<h1>Вы на странице Django Test</h1>")