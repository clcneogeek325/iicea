from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.perfil.models import perfil
from .forms import perfilForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_lista_perfiles(request):
	contact_list = perfil.objects.order_by('id').reverse()
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
	return render_to_response("perfil/lista.html",ctx,
			context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
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
@login_required(login_url=URL_LOGIN)
def view_add_pefil(request):
	if request.method == "POST":
		form = perfilForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.activo = True
			p.save()
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
				
@login_required(login_url=URL_LOGIN)
def view_del_perfil(request,id):
	p = perfil.objects.get(pk=id)
	p.activo = False
	p.save()
	return HttpResponseRedirect('/perfil/')
	
