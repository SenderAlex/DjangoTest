from django.urls import path
from .import views

urlpatterns = [
    path('goats', views.goats, name='goats'),
    path('add_player', views.add_player, name='add_player'),
    ]