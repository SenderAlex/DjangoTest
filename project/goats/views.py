from django.shortcuts import render, redirect
from .models import Goat
from .forms import GoatForm

def goats(request):
    goats = Goat.objects.all().order_by('-scores')
    return render(request, "goats/goats.html", {"goats": goats})

def add_player(request):
    error = ''
    if request.method == 'POST':
        form = GoatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goats')
        else:
            error = 'Данные введены не корректно'
    form = GoatForm()
    return render(request, "goats/add_top_scorer.html", {"form": form, "error": error})