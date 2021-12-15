from django.urls import path
from . import views
from Gry.views import *

urlpatterns = [
    path('gra/<id>/', gra, name='gra'),
    path('', index),
    path('gryapi/', views.GryAPI.as_view()),
    path('gryapi/<int:pk>/', views.GryAPI.as_view()),
    path('katapi/', views.KategoriaAPI.as_view()),
    path('katapi/<int:pk>/', views.KategoriaAPI.as_view()),
    path('prodapi/', views.ProducentAPI.as_view()),
    path('prodapi/<int:pk>/', views.ProducentAPI.as_view())
]