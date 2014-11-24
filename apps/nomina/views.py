from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import nomina
from .forms import nominaForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_eliminar_nomina(request,id):
	n = nomina.objects.get(pk=id)
	n.activo = False
	n.save()
	return HttpResponseRedirect('/nomina/')

@login_required(login_url=URL_LOGIN)
def view_lista_nominas(request):
	contact_list = nomina.objects.order_by('id').reverse()
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
	return render_to_response("nomina/lista.html",ctx,
			context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_add_nomina(request):
	if request.method == "POST":
		form  = nominaForm(request.POST)
		if form.is_valid():
			a = form.save(commit=False)
			a.activo = True
			a.save()
			return HttpResponseRedirect("/nomina/")
		else:
			form  = nominaForm(request.POST)
			ctx = {'form':form}
			return render_to_response('nomina/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = nominaForm()
		ctx = {'form':form}
		return render_to_response('nomina/add.html',ctx,
				context_instance=RequestContext(request))



@login_required(login_url=URL_LOGIN)
def view_editar_nomina(request,id):
	try:
		n = nomina.objects.get(pk=id)
		if request.method == "POST":
			form  = nominaForm(request.POST,instance=n)
			if form.is_valid():
				a = form.save(commit=False)
				a.activo = True
				a.save()
				return HttpResponseRedirect("/nomina/")
			else:
				form  = nominaForm(request.POST)
				ctx = {'form':form}
				return render_to_response('nomina/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = nominaForm(instance=n)
			ctx = {'form':form}
			return render_to_response('nomina/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

