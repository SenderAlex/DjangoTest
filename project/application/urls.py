from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('laliga/', views.laliga, name='laliga'),
    path('premiereleague/', views.premiereleague, name='premiereleague'),
    path('seriea/', views.seriea, name='seriea'),
    path('bundesliga/', views.bundesliga, name='bundesliga'),
    path('liga1/', views.liga1, name='liga1')
]