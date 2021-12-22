from django.db import models

# Create your models here.


class KategoriaGry(models.Model):
    nazwa = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'KategoriaGry'
        verbose_name_plural = 'KategorieGier'

    def __str__(self):
        return self.nazwa


class ProducentGry(models.Model):
    nazwa = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'ProducentGry'
        verbose_name_plural = 'ProducenciGier'

    def __str__(self):
        return self.nazwa


class Gry(models.Model):
    nazwaGry = models.CharField(max_length=250)
    kategoria = models.ForeignKey(KategoriaGry, related_name='gry', on_delete=models.SET_NULL, null=True)
    dataWydania = models.DateField()
    producent = models.ForeignKey(ProducentGry, related_name='gry', on_delete=models.SET_NULL, null=True)
    opis = models.CharField(max_length=300)
    owner = models.ForeignKey('auth.User', related_name='gry', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Gra'
        verbose_name_plural = 'Gry'

    def __str__(self):
        return self.nazwaGry


