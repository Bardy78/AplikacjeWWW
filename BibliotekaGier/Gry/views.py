from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from .models import Gry, ProducentGry, KategoriaGry
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import GraSerializer, KategoriaSerializer, ProducentSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt

def index (request):
     kategorie = KategoriaGry.objects.all()
     return HttpResponse(kategorie)



def gra(request, id):
   gra_user = Gry.objects.get(pk=id)
   dane = "<h1>" + str(gra_user.nazwaGry) + "</h1>" + \
           "<p>" + str(gra_user.producent) + "</p>" + \
           "<p>" + str(gra_user.kategoria) + "</p>" + \
           "<p>" + str(gra_user.dataWydania) + "</p>" + \
           "<p>" + str(gra_user.opis) + "</p>"
   return HttpResponse(dane)

class GryAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            gra = Gry.objects.get(id=id)
            serializer = GraSerializer(gra)
            return Response(serializer.data)

        gra = Gry.objects.all()
        serializer = GraSerializer(gra, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serialzer = GraSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class KategoriaAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            kategoria = KategoriaGry.objects.get(id=id)
            serializer = KategoriaSerializer(kategoria)
            return Response(serializer.data)

        kategoria =KategoriaGry.objects.all()
        serializer = KategoriaSerializer(kategoria, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serialzer = KategoriaSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            producent = ProducentGry.objects.get(id=id)
            serializer = ProducentSerializer(producent)
            return Response(serializer.data)

        producent =ProducentGry.objects.all()
        serializer = ProducentSerializer(producent, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serialzer = ProducentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)