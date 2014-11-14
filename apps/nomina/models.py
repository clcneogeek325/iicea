from django.db import models
from apps.empleado.models import empleado


class nomina(models.Model):
	empleado = models.ForeignKey(empleado)
	cantidad = models.FloatField()
	fecha = models.DateTimeField(blank=False, null=False,auto_now_add=True)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.empleado.empleado.first_name

