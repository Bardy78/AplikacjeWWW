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
        ordering = ('nazwa',)
    def __str__(self):
        return self.nazwa

class Gry(models.Model):
    nazwaGry=models.CharField(max_length=250)
    kategoria = models.ForeignKey(KategoriaGry, related_name="gry", on_delete=models.CASCADE)
    dataWydania = models.DateField()
    producent = models.ForeignKey(ProducentGry, related_name="gry", on_delete=models.CASCADE)
    opis = models.CharField(max_length=300)

    class Meta:
        ordering=('nazwaGry',)

    def __str__(self):
        return self.nazwaGry


