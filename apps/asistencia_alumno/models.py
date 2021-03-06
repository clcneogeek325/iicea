from django.db import models
from apps.alumno.models import alumno
from apps.empleado.models import empleado
from apps.horario.models import horario


class asistencia_alumno(models.Model):
	empleado= models.ForeignKey(empleado)
	alumno = models.ManyToManyField(alumno)
	horario = models.ForeignKey(horario)
	fecha = models.DateField(blank=False, null=False,unique=True)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		str_fecha= str(self.fecha)
		return str_fecha


