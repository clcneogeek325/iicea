from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import asistencia_alumno
from .forms import asistencia_alumnoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

def view_lista_asistencia_alumnos(request):
	lista = asistencia_alumno.objects.all()
	ctx = {'lista':lista}
	return render_to_response("asistencia_alumno/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_asistencia_alumno(request,id):
	try:
		ast = asistencia_alumno.objects.get(pk=id)
		if request.method == "POST":
			form  = asistencia_alumnoForm(request.POST,instance=ast)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/asistencia_alumno/")
			else:
				form  = asistencia_alumnoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('asistencia_alumno/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = asistencia_alumnoForm(instance=g)
			ctx = {'form':form}
			return render_to_response('asistencia_alumno/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

