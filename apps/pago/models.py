from django.db import models
from apps.alumno.models import alumno
from apps.concepto_pago.models import concepto_pago

class pago(models.Model):
	alumno = models.ForeignKey(alumno,null=False,blank=False)
	concepto_pago = models.ForeignKey(concepto_pago,null=False,blank=False)
	fecha = models.DateTimeField(blank=False, null=False,auto_now_add=True)
	cantidad = models.FloatField()
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.alumno.alumno.first_name



