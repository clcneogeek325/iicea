from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import calificacion
from .forms import calificacionForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.semestre.models import semestre
from apps.alumno.models import alumno
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def view_eliminar_calificacion(request,id):
	c = calificacion.objects.get(pk=id)
	c.activo = False
	c.save()
	return HttpResponseRedirect('/calificacion/')


def view_calificaciones_alumno(request):
	lista = semestre.objects.filter(activo=True)
	ctx = {'lista':lista}
	return render_to_response("calificacion/semestres.html",ctx,
			context_instance=RequestContext(request))

def view_calificaciones_alumno_x_semestre(request,id_semestre,id_user):
	
	s = semestre.objects.get(pk=id_semestre)	
	a = alumno.objects.get(alumno_id=id_user)
	lista = calificacion.objects.filter(alumno=a,semestre=s)
	ctx = {'lista':lista}
	return render_to_response("calificacion/calificaciones.html",ctx,
			context_instance=RequestContext(request))
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def view_lista_calificacions(request):
	contact_list = calificacion.objects.order_by('id').reverse()
	paginator = Paginator(contact_list, 3)# Show 25 contacts per page
	page = request.GET.get('page')
	try:
		lista = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		lista = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		lista = paginator.page(paginator.num_pages)
	ctx = {'lista':lista}
	return render_to_response("calificacion/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_calificacion(request,id):
	try:
		a = calificacion.objects.get(pk=id)
		if request.method == "POST":
			form  = calificacionForm(request.POST,instance=a)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/calificacion/")
			else:
				print "no valido",form.errors
				form  = calificacionForm(request.POST)
				ctx = {'form':form}
				return render_to_response('calificacion/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = calificacionForm(instance=a)
			ctx = {'form':form}
			return render_to_response('calificacion/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))


def view_agregar_calificacion(request):
	if request.method == "POST":
		form  = calificacionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/calificacion/")
		else:
			form  = calificacionForm(request.POST)
			ctx = {'form':form}
			return render_to_response('calificacion/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = calificacionForm()
		ctx = {'form':form}
		return render_to_response('calificacion/add.html',ctx,
				context_instance=RequestContext(request))
				
				

