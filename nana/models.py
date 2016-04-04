# -*- coding: UTF-8 -*-
from django.db import models

from django.contrib.auth.models import User

class fecha(models.Model):
	anio		= models.IntegerField()
	
class imagen(models.Model):
	titulo      = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	imagen_g    = models.FileField(max_length=20)
	fecha		= models.ForeignKey(fecha)

