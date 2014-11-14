from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import materia
from .forms import materiaForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def view_lista_materias(request):
	lista = materia.objects.all()
	ctx = {'lista':lista}
	return render_to_response("materia/lista.html",ctx,
			context_instance=RequestContext(request))

def view_add_materia(request):
	if request.method == "POST":
		form  = materiaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/materia/")
		else:
			form  = materiaForm(request.POST)
			ctx = {'form':form}
			return render_to_response('materia/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = materiaForm()
		ctx = {'form':form}
		return render_to_response('materia/add.html',ctx,
				context_instance=RequestContext(request))

def view_editar_materia(request,id):
	try:
		m = materia.objects.get(pk=id)
		if request.method == "POST":
			form  = materiaForm(request.POST,instance=m)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/materia/")
			else:
				form  = materiaForm(request.POST)
				ctx = {'form':form}
				return render_to_response('materia/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = materiaForm(instance=m)
			ctx = {'form':form}
			return render_to_response('materia/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

