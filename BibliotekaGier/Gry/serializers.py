from rest_framework import serializers
from .models import Gry, ProducentGry, KategoriaGry


class GraSerializer(serializers.HyperlinkedModelSerializer):
    kategoria = serializers.SlugRelatedField(queryset=KategoriaGry.objects.all(), slug_field='nazwa')
    producent = serializers.SlugRelatedField(queryset=ProducentGry.objects.all(), slug_field='nazwa')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Gry
        fields = ['url', 'id', 'nazwaGry', 'kategoria','owner', 'dataWydania', 'producent', 'opis']


class KategoriaSerializer(serializers.HyperlinkedModelSerializer):
    gry = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='gry-detail')

    class Meta:
        model = KategoriaGry
        fields = ['url', 'id', 'nazwa', 'gry']


class ProducentSerializer(serializers.HyperlinkedModelSerializer):
    gry = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='gry-detail')

    class Meta:
        model = ProducentGry
        fields = ['url', 'id', 'nazwa', 'gry']




