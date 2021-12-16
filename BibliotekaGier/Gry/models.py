from django.db import models

# Create your models here.
class KategoriaGry(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.nazwa

class ProducentGry(models.Model):
    nazwa = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.nazwa

class Gry(models.Model):
    nazwaGry=models.CharField(max_length=250)
    kategoria = models.ForeignKey(KategoriaGry, related_name='kategorias', on_delete=models.SET_NULL, null=True)
    dataWydania = models.DateField()
    producent = models.ForeignKey(ProducentGry, related_name='producents', on_delete=models.SET_NULL, null=True)
    opis = models.CharField(max_length=300)

    class Meta:
        ordering=('id',)

    def __str__(self):
        return self.nazwaGry


