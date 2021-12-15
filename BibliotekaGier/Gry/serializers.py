from rest_framework import serializers
from .models import Gry, ProducentGry, KategoriaGry



class GraSerializer(serializers.ModelSerializer):
    kategoria = serializers.SlugRelatedField(queryset=KategoriaGry.objects.all(), slug_field='nazwa')
    dataWydania = serializers.DateField()
    producent = serializers.SlugRelatedField(queryset=ProducentGry.objects.all(), slug_field='nazwa')

    class Meta:
        model = Gry
        fields = ['id', 'nazwaGry', 'kategoria', 'dataWydania', 'producent', 'opis']

class KategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = KategoriaGry
        fields = ['id', 'nazwa']


class ProducentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducentGry
        fields = ['id', 'nazwa']




