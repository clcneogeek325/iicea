from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.semestre.models import semestre
from .forms import semestreForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def view_add_semestre(request):
	if request.method == "POST":
		form = semestreForm(request.POST)
		if form.is_valid():
			s = form.save(commit=False)
			s.activo = True
			s.save()
			return HttpResponseRedirect('/semestre/')
		else:
			form = semestreForm(request.POST)
			ctx = {'form':form}
			return render_to_response('semestre/add.html',ctx,
					context_instance=RequestContext(request))
	else:
		 form = semestreForm()
		 ctx = {'form':form}
		 return render_to_response('semestre/add.html',ctx,
				 context_instance=RequestContext(request))
	
	


def view_lista_semestres(request):
	lista = semestre.objects.filter(activo=True)
	ctx = {'lista':lista}
	return render_to_response("semestre/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_semestre(request,id):
	try:
		s = semestre.objects.get(pk=id)
		if request.method == "POST":
			form  = semestreForm(request.POST,instance=s)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/semestre/")
			else:
				form  = semestreForm(request.POST)
				ctx = {'form':form}
				return render_to_response('semestre/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = semestreForm(instance=s)
			ctx = {'form':form}
			return render_to_response('semestre/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
def view_del_semestre(request,id):
	p = semestre.objects.get(pk=id)
	p.activo = False
	p.save()
	return HttpResponseRedirect('/semestre/')
	


