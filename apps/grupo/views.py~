from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.grupo.models import grupo
from .forms import grupoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist



def view_add_grupo(request):
	if request.method == "POST":
		form = grupoForm(request.POST)
		if form.is_valid():
			g = form.save(commit=False)
			g.activo = True
			g.save()
			return HttpResponseRedirect('/grupo/')
		else:
			form = grupoForm(request.POST)
			ctx = {'form':form}
			return render_to_response('grupo/add.html',ctx,
					context_instance=RequestContext(request))
	else:
		form = grupoForm()
		ctx = {'form':form}
		return render_to_response('grupo/add.html',ctx,
				context_instance=RequestContext(request))
	


def view_lista_grupos(request):
	lista = grupo.objects.filter(activo=True)
	ctx = {'lista':lista}
	return render_to_response("grupo/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_grupo(request,id):
	try:
		g = grupo.objects.get(pk=id)
		if request.method == "POST":
			form  = grupoForm(request.POST,instance=g)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/grupo/")
			else:
				form  = grupoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('grupo/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = grupoForm(instance=g)
			ctx = {'form':form}
			return render_to_response('grupo/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
					
def view_del_grupo(request,id):
	g = grupo.objects.get(pk=id)
	g.activo = False
	g.save()
	return HttpResponseRedirect('/grupo/')

