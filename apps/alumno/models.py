from django.db import models
from django.contrib.auth.models import User
from apps.semestre.models import semestre
from apps.grupo.models import grupo
from apps.tutor.models import tutor
from apps.horario.models import horario
from apps.materia.models import materia
from apps.semestre.models import semestre
class alumno(models.Model):
	TIPO_SEXO = (
	('Hombre', 'Hombre'),
	('Mujer', 'Mujer'),
	)
	DIAS = (
	('lunes','lunes'),
	('martes','martes'),
	('miercoles','miercoles'),
	('jueves','jueves'),
	('viernes','viernes'),
	('sabado','sabado'),
	('domingo','domingo'),
	('lunes','lunes'),
	)
	alumno = models.OneToOneField(User,unique=True)
	sexo = models.CharField(choices=TIPO_SEXO,max_length=20,null=True)
	curp = models.CharField(max_length=20,null=True)
	fecha_nacimiento = models.DateField(null=True)
	localidad = models.CharField(max_length=30,null=True)
	municipio = models.CharField(max_length=30,null=True)
	email = models.CharField(max_length=30,null=True)
	dia = models.CharField(choices=DIAS,max_length=20,null=True)
	telefono = models.CharField(max_length=20,null=True)
	grupo = models.ForeignKey(grupo,null=True)
	tutor = models.ForeignKey(tutor,null=True)
	horario = models.ForeignKey(horario,null=True)
	materias = models.ManyToManyField(materia,null=True)
	semestre = models.ManyToManyField(semestre,null=True)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.alumno.first_name
		
