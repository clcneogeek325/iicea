from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.tutor.models import tutor
from .forms import tutorForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist



def view_add_tutor(request):
	if request.method == "POST":
		form  = tutorForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/tutor/")
		else:
			form  = tutorForm(request.POST)
			ctx = {'form':form}
			return render_to_response('tutor/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = tutorForm()
		ctx = {'form':form}
		return render_to_response('tutor/add.html',ctx,
				context_instance=RequestContext(request))


def view_lista_tutores(request):
	lista = tutor.objects.all()
	ctx = {'lista':lista}
	return render_to_response("tutor/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_tutor(request,id):
	try:
		t = tutor.objects.get(pk=id)
		if request.method == "POST":
			form  = tutorForm(request.POST,instance=t)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/tutor/")
			else:
				form  = tutorForm(request.POST)
				ctx = {'form':form}
				return render_to_response('tutor/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = tutorForm(instance=t)
			ctx = {'form':form}
			return render_to_response('tutor/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

