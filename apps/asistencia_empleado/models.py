from django.db import models
from apps.empleado.models import empleado

class asistencia_empleado(models.Model):
	empleado = models.ForeignKey(empleado,blank=False,null=False)
	hora_entrada = models.TimeField(blank=False, null=False)
	hora_salida = models.TimeField(blank=False, null=False)
	fecha = models.DateField(blank=False, null=False)

