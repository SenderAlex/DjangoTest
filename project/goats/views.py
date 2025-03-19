from django.shortcuts import render
from .models import Goat

def goats(request):
    goats = Goat.objects.all()
    return render(request, "goats/goats.html", {"goats": goats})