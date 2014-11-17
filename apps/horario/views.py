from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import horario
from .forms import horarioForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def view_lista_horarios(request):
	lista = horario.objects.filter(activo=True)
	ctx = {'lista':lista}
	return render_to_response("horario/lista.html",ctx,
			context_instance=RequestContext(request))

def view_add_horario(request):
	if request.method == "POST":
		form  = horarioForm(request.POST)
		if form.is_valid():
			h = form.save(commit=False)
			h.activo = True
			h.save()
			return HttpResponseRedirect("/horario/")
		else:
			form  = horarioForm(request.POST)
			ctx = {'form':form}
			return render_to_response('horario/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = horarioForm()
		ctx = {'form':form}
		return render_to_response('horario/add.html',ctx,
				context_instance=RequestContext(request))

def view_editar_horario(request,id):
	try:
		h = horario.objects.get(pk=id)
		if request.method == "POST":
			form  = horarioForm(request.POST,instance=h)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/horario/")
			else:
				form  = horarioForm(request.POST)
				ctx = {'form':form}
				return render_to_response('horario/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = horarioForm(instance=h)
			ctx = {'form':form}
			return render_to_response('horario/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

def view_del_horario(request,id):
	h = horario.objects.get(pk=id)
	h.activo = False
	h.save()
	return HttpResponseRedirect('/horario/')
	
