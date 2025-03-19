from django.urls import path
from .import views

urlpatterns = [
    path('goats/', views.goats, name='goats')
    ]