from django.db import models
from apps.alumno.models import alumno

class asistencia_alumno(models.Model):
	alumno = models.ForeignKey(alumno,blank=False,null=False)
	hora_entrada = models.TimeField(blank=False, null=False)
	hora_salida = models.TimeField(blank=False, null=False)
	fecha = models.DateField(blank=False, null=False)


