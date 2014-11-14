from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import calificacion
from .forms import calificacionForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def view_lista_calificacions(request):
	lista = calificacion.objects.all()
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

