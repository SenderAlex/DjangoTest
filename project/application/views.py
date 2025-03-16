from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "application/index.html")


def laliga(request):
    return render(request, "application/laliga.html")


def premiereleague(request):
    return render(request, "application/premiereleague.html")

def seriea(request):
    return render(request, "application/seriea.html")


def bundesliga(request):
    return render(request, "application/bundesliga.html")

def liga1(request):
    return render(request, "application/liga1.html")