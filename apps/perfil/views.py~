from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.perfil.models import perfil
from .forms import perfilForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def view_lista_perfiles(request):
	lista = perfil.objects.all()
	ctx = {'lista':lista}
	return render_to_response("perfil/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_perfil(request,id):
	try:
		p = perfil.objects.get(pk=id)
		if request.method == "POST":
			form  = perfilForm(request.POST,instance=p)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/perfil/")
			else:
				form  = perfilForm(request.POST,instance=p)
				ctx = {'form':form}
				return render_to_response('perfil/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = perfilForm(instance=p)
			ctx = {'form':form}
			return render_to_response('perfil/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

def view_add_pefil(request):
	if request.method == "POST":
		form = perfilForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/perfil/')

		else:
			form = perfilForm(request.POST)
			ctx = {'form':form}
			return render_to_response("perfil/add.html",ctx,
					context_instance=RequestContext(request))

	else:
		form = perfilForm()
		ctx = {'form':form}
		return render_to_response("perfil/add.html",ctx,
				context_instance=RequestContext(request))
