from .models import Gry, ProducentGry, KategoriaGry
from rest_framework.response import Response
from .serializers import GraSerializer, KategoriaSerializer, ProducentSerializer
from rest_framework import generics
from rest_framework.reverse import reverse


class RootApi(generics.GenericAPIView):
    name = 'root-api'

    def get(self, request, *args, **kwargs):
        return Response({
            'gry': reverse(GryList.name, request=request),
            'kategoria': reverse(KatList.name, request=request),
            'producent': reverse(ProdList.name, request=request),
        })


class GryList(generics.ListCreateAPIView):
    queryset = Gry.objects.all()
    serializer_class = GraSerializer
    name = 'gry-list'


class GraAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gry.objects.all()
    serializer_class = GraSerializer
    name = 'gry-detail'


class KatList(generics.ListCreateAPIView):
    queryset = KategoriaGry.objects.all()
    serializer_class = KategoriaSerializer
    name = 'KatList'


class KatApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = KategoriaGry.objects.all()
    serializer_class = KategoriaSerializer
    name = 'KatDet'


class ProdList(generics.ListCreateAPIView):
    queryset = ProducentGry.objects.all()
    serializer_class = ProducentSerializer
    name = 'ProdList'


class ProdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProducentGry.objects.all()
    serializer_class = ProducentSerializer
    name = 'ProdDet'






