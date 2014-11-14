from django.db import models
from apps.alumno.models import alumno
from apps.empleado.models import empleado
class asistencia_alumno(models.Model):
	empleado= models.ForeignKey(empleado,blank=False,null=False)
	alumnos = models.ManyToManyField(alumno,blank=False,null=False)
	hora_entrada = models.TimeField(blank=False, null=False)
	hora_salida = models.TimeField(blank=False, null=False)
	fecha = models.DateField(blank=False, null=False)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		str_fecha= str(self.fecha)
		return str_fecha



