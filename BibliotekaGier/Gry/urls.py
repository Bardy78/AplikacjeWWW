from django.urls import path
from . import views, views2


urlpatterns = [
    #path('gra/<id>/', gra, name='gra'),
    # path('gryapi/', views.GryAPI.as_view()),
    # path('gryapi/<int:pk>/', views.GryAPI.as_view()),
    path('kat/', views2.KatList.as_view(), name=views2.KatList.name),
    path('kat/<int:pk>/', views2.KatApi.as_view(), name=views2.KatList.name),
    path('prod/', views2.ProdList.as_view(), name=views2.ProdList.name),
    path('prod/<int:pk>/', views2.ProdApi.as_view(), name=views2.ProdApi.name),
    path('gry/', views2.GryList.as_view(), name=views2.GryList.name),
    path('gry/<int:pk>/', views2.GraAPI.as_view(), name=views2.GraAPI.name),
    path('', views2.RootApi.as_view(), name=views2.RootApi.name)

]
