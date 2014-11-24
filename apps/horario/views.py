from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import horario
from .forms import horarioForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_lista_horarios(request):
	contact_list = horario.objects.order_by('id').reverse()
	paginator = Paginator(contact_list, 3)# Show 25 contacts per page
	page = request.GET.get('page')
	try:
		lista = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		lista = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		lista = paginator.page(paginator.num_pages)
	ctx = {'lista':lista}
	return render_to_response("horario/lista.html",ctx,
			context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
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

@login_required(login_url=URL_LOGIN)
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

@login_required(login_url=URL_LOGIN)
def view_del_horario(request,id):
	h = horario.objects.get(pk=id)
	h.activo = False
	h.save()
	return HttpResponseRedirect('/horario/')
	
