from rest_framework import serializers
from .models import Gry, ProducentGry, KategoriaGry



class GraSerializer(serializers.HyperlinkedModelSerializer):
    # dataWydania = serializers.DateField()
    #kategoria = serializers.HyperlinkedRelatedField(read_only=True, view_name='KatDet')
    #producent = serializers.HyperlinkedRelatedField(read_only=True, view_name='ProdDet')
    kategoria = serializers.SlugRelatedField(queryset=KategoriaGry.objects.all(), slug_field='nazwa')
    producent = serializers.SlugRelatedField(queryset=ProducentGry.objects.all(), slug_field='nazwa')

    class Meta:
        model = Gry
        fields = ['url', 'id', 'nazwaGry', 'kategoria', 'dataWydania', 'producents', 'opis']

class KategoriaSerializer(serializers.HyperlinkedModelSerializer):
    nazwa = serializers.HyperlinkedRelatedField(read_only=True, view_name='KatDet')
    class Meta:
        model = KategoriaGry
        fields = ['url', 'id', 'nazwa']


class ProducentSerializer(serializers.HyperlinkedModelSerializer):
    nazwa = serializers.HyperlinkedRelatedField(read_only=True, view_name='ProdDet')
    class Meta:
        model = ProducentGry
        fields = ['url', 'id', 'nazwa']




