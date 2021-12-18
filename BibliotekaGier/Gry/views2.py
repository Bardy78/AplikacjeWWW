from .models import Gry, ProducentGry, KategoriaGry
from rest_framework.response import Response
from .serializers import GraSerializer, KategoriaSerializer, ProducentSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from django_filters import FilterSet, DateFilter
from rest_framework import permissions

class RootApi(generics.GenericAPIView):
    name = 'root-api'

    def get(self, request, *args, **kwargs):
        return Response({
            'gry': reverse(GryList.name, request=request),
            'kategoriaGry': reverse(KategoriaGryList.name, request=request),
            'producentGry': reverse(ProdList.name, request=request),
        })


class GryFilter(FilterSet):
    from_date = DateFilter(field_name='dataWydania',lookup_expr='gte')
    to_date = DateFilter(field_name='dataWydania', lookup_expr='lte')
    class Meta:
        model = Gry
        fields = ('from_date', 'to_date', 'nazwaGry', 'kategoria')


class GryList(generics.ListCreateAPIView):
    queryset = Gry.objects.all()
    serializer_class = GraSerializer
    name = 'gry-list'
    filter_class = GryFilter
    filterset_fields = ['nazwaGry', 'kategoria']
    search_fields = ['nazwaGry']
    ordering_fields = ['nazwaGry', 'kategoria']
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GraAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gry.objects.all()
    serializer_class = GraSerializer
    name = 'gry-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KategoriaGryList(generics.ListCreateAPIView):
    queryset = KategoriaGry.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoriagry-list'
    filterset_fields = ['nazwa']
    search_fields = ['nazwa']
    ordering_fields = ['nazwa']
    permission_classes = [permissions.IsAuthenticated]

class KategoriaGryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KategoriaGry.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoriagry-detail'
    permission_classes = [permissions.IsAuthenticated]


class ProdList(generics.ListCreateAPIView):
    queryset = ProducentGry.objects.all()
    serializer_class = ProducentSerializer
    name = 'producentgry-list'
    filterset_fields = ['nazwa']
    search_fields = ['nazwa']
    ordering_fields = ['nazwa']
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class ProdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProducentGry.objects.all()
    serializer_class = ProducentSerializer
    name = 'producentgry-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
