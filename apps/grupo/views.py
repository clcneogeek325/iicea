from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.grupo.models import grupo
from .forms import grupoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
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
	

@login_required(login_url=URL_LOGIN)
def view_lista_grupos(request):
	contact_list = grupo.objects.order_by('id').reverse()
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
	return render_to_response("grupo/lista.html",ctx,
			context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
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
			ctx = {'msg':"No se encontro el grupo solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_del_grupo(request,id):
	try:
		g = grupo.objects.get(pk=id)
		g.activo = False
		g.save()
		return HttpResponseRedirect('/grupo/')
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el grupo solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
