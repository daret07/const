# -*- coding: UTF-8 -*-
from django.db import models

from django.contrib.auth.models import User

class fecha(models.Model):
  anio    = models.IntegerField()

  def __str__(self):
    return str(self.anio)


class imagen(models.Model):
	titulo      = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	imagen_g    = models.FileField(max_length=20)
	logo		= models.FileField(max_length=20)
	fecha		= models.ForeignKey(fecha)

	def __str__(self):
		return unicode(self.titulo)

class galeria(models.Model):
	img         = models.FileField(max_length=50)
	padre		= models.ForeignKey(imagen)

class imagen_galeria_principal(models.Model):
  imagen_principal    = models.FileField(max_length=50)
  Galeria             = models.ForeignKey(imagen)


class equipo(models.Model):
  foto        = models.FileField(max_length=20,blank=True,null=True)
  nombre      = models.CharField(max_length=50,blank=True,null=True)
  puesto      = models.CharField(max_length=100,blank=True,null=True)
  correo      = models.CharField(max_length=100,blank=True,null=True)
  descripcion = models.CharField(max_length=500,blank=True,null=True)
  logo        = models.FileField(max_length=20,blank=True,null=True)
