from django.shortcuts import render


def goats(request):
    return render(request, "goats/goats.html")