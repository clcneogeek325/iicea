from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import asistencia_empleado
from .forms import asistencia_empleadoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

def view_lista_asistencia_empleados(request):
	lista = asistencia_empleado.objects.all()
	ctx = {'lista':lista}
	return render_to_response("asistencia_empleado/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_asistencia_empleado(request,id):
	try:
		ast = asistencia_empleado.objects.get(pk=id)
		if request.method == "POST":
			form  = asistencia_empleadoForm(request.POST,instance=ast)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/asistencia_empleado/")
			else:
				form  = asistencia_empleadoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('asistencia_empleado/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = asistencia_empleadoForm(instance=ast)
			ctx = {'form':form}
			return render_to_response('asistencia_empleado/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

def view_add_asistencia_empleado(request):
	if request.method == "POST":
		form  = asistencia_empleadoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/asistencia_empleado/")
		else:
			form  = asistencia_empleadoForm(request.POST)
			ctx = {'form':form}
			return render_to_response('asistencia_empleado/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = asistencia_empleadoForm()
		ctx = {'form':form}
		return render_to_response('asistencia_empleado/add.html',ctx,
				context_instance=RequestContext(request))

