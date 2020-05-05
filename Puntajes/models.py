from django.db import models

# Create your models here.
class Score(models.Model):
    juego = models.CharField(max_length=100)
    jugador = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    tiempo = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)

    class Meta:
        ordering = ['tiempo']

    @classmethod
    def create(cls, juego, jugador, nivel, tiempo, fecha):
        score = cls(juego = juego, jugador = jugador, nivel = nivel, tiempo = tiempo, fecha = fecha)
        return score
