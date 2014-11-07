from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.observacion.models import observacion
from .forms import observacionForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def view_lista_observaciones(request):
	lista = observacion.objects.all()
	ctx = {'lista':lista}
	return render_to_response("observacion/lista.html",ctx,
			context_instance=RequestContext(request))

def view_add_observacion(request):
	if request.method == "POST":
		form  = observacionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/observacion/")
		else:
			form  = observacionForm(request.POST)
			ctx = {'form':form}
			return render_to_response('observacion/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = observacionForm()
		ctx = {'form':form}
		return render_to_response('observacion/add.html',ctx,
					context_instance=RequestContext(request))

def view_editar_observacion(request,id):
	try:
		o = observacion.objects.get(pk=id)
		if request.method == "POST":
			form  = observacionForm(request.POST,instance=o)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/observacion/")
			else:
				form  = observacionForm(request.POST)
				ctx = {'form':form}
				return render_to_response('observacion/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = observacionForm(instance=o)
			ctx = {'form':form}
			return render_to_response('observacion/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

