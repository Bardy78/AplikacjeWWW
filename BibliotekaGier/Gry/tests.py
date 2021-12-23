from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views2
from .models import KategoriaGry, Gry, ProducentGry
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User


class KategoriaGryTests(APITestCase):
    def post_kategoria_gry(self, nazwa):
        url = reverse(views2.KategoriaGryList.name)
        data = {'nazwa': nazwa}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_kategoria_gry(self):
        new_kategoria_gry_name = 'FPS'
        response = self.post_kategoria_gry(new_kategoria_gry_name)
        print("PK {0}".format(KategoriaGry.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert KategoriaGry.objects.count() == 1
        assert KategoriaGry.objects.get().nazwa == new_kategoria_gry_name

    def test_post_existing_kategoria_gry_name(self):
        url = reverse(views2.KategoriaGryList.name)
        new_kategoria_gry_name = 'FPS'
        data = {'nazwa': new_kategoria_gry_name}
        response_one = self.post_kategoria_gry(new_kategoria_gry_name)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_kategoria_gry(new_kategoria_gry_name)
        print(response_one)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_kategoria_gry_by_name(self):
        kategoria_gry_name_one = 'FPS'
        kategoria_gry_name_two = 'Sportowe'
        self.post_kategoria_gry(kategoria_gry_name_one)
        self.post_kategoria_gry(kategoria_gry_name_two)
        filter_by_name = {'nazwa': kategoria_gry_name_two}
        url = '{0}?{1}'.format(reverse(views2.KategoriaGryList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_get_kategoria_gry_collection(self):
        new_kategoria_gry_name = 'Symulacja'
        self.post_kategoria_gry(new_kategoria_gry_name)
        url = reverse(views2.KategoriaGryList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['nazwa'] == new_kategoria_gry_name

    def test_update_kategoria_gry(self):
        kategoria_gry_name = 'FPS'
        response = self.post_kategoria_gry(kategoria_gry_name)
        url = urls.reverse(views2.KategoriaGryDetail.name, None, {response.data['id']})
        updated_kategoria_gry_name = 'Strzelanka'
        data = {'nazwa': updated_kategoria_gry_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['nazwa'] == updated_kategoria_gry_name

    def test_get_kategoria_gry(self):
        kategoria_gry_name = 'FPS'
        response = self.post_kategoria_gry(kategoria_gry_name)
        url = urls.reverse(views2.KategoriaGryDetail.name, None, {response.data['id']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['nazwa'] == kategoria_gry_name


# class GryTests(APITestCase):
#     def create_kategoria_gry(self, client):
#         url = reverse(views2.KategoriaGryList.name)
#         data = {'id': 1, 'nazwa': 'wyścigi'}
#         client.post(url, data, format='json')
#
#     def create_gry(self, nazwagry, kategoria_gry, datawydania, producent, opis, owner, client):
#         url = reverse(views2.GryList.name)
#         data = {'nazwaGry': nazwagry,
#                 'kategoria': kategoria_gry,
#                 'dataWydania': datawydania,
#                 'producent': producent,
#                 'opis': opis,
#                 'owner': owner}
#         response = client.post(url, data, format='json')
#         return response
#
#     def test_post_and_get_gry(self):
#         user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
#         client = APIClient()
#         client.login(username='admin1', password='admin123')
#         self.create_kategoria_gry(client)
#         new_nazwagry = 'Counter-Strike 1.6'
#         new_kategoria_gry = 'FPS'
#         new_datawydania = '2001-01-01'
#         new_producent = 'Valve'
#         new_opis = 'Taktyczna gra'
#         new_owner = 'admin'
#         response = self.create_gry(new_nazwagry, new_kategoria_gry, new_datawydania, new_producent, new_opis, new_owner,
#                                    client)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert Gry.objects().count == 1
#         assert Gry.objects().get == new_nazwagry
#         assert Gry.objects().get == new_producent
