from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import asistencia_alumno
from .forms import asistencia_alumnoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

def view_lista_asistencia_alumnos(request):
	lista = asistencia_alumno.objects.filter(activo=True)
	ctx = {'lista':lista}
	return render_to_response("asistencia_alumno/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_asistencia_alumno(request,id):
	try:
		ast = asistencia_alumno.objects.get(pk=id)
		if request.method == "POST":
			form  = asistencia_alumnoForm(request.POST,instance=ast)
			if form.is_valid(commit=False):
				form.save_m2m()
				aa.activo=True
				aa.save()
				return HttpResponseRedirect("/asistencia_alumno/")
			else:
				form  = asistencia_alumnoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('asistencia_alumno/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = asistencia_alumnoForm(instance=ast)
			ctx = {'form':form}
			return render_to_response('asistencia_alumno/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

def view_add_asistencia_alumno(request):
	if request.method == "POST":
		form  = asistencia_alumnoForm(request.POST)
		if form.is_valid():
			aa = form.save(commit=False)
			form.save_m2m()
			aa.activo = False
			aa.save()
			return HttpResponseRedirect("/asistencia_alumno/")
		else:
			form  = asistencia_alumnoForm(request.POST)
			ctx = {'form':form}
			return render_to_response('asistencia_alumno/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = asistencia_alumnoForm()
		ctx = {'form':form}
		return render_to_response('asistencia_alumno/add.html',ctx,
				context_instance=RequestContext(request))

