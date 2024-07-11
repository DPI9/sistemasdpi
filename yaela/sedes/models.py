# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Sede(models.Model):
    idsede = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.sede
    
class TipoCampo(models.Model):
    idtipocampo = models.AutoField(primary_key=True)
    tipocampo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipocampo

class Campo(models.Model):
    idcampo = models.AutoField(primary_key=True)
    campo = models.CharField(max_length=100)
    idsede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    idtipocampo = models.ForeignKey(TipoCampo, on_delete=models.CASCADE)

    def __str__(self):
        return self.campo
