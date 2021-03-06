from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.observacion.models import observacion
from .forms import observacionForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_eliminar_observacion(request,id):
	try:
		o = observacion.objects.get(pk=id)
		o.activo = False
		o.save()
		return HttpResponseRedirect('/observacion/')
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el observacion solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_lista_observaciones(request):
	contact_list = observacion.objects.order_by('id').reverse()
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
	return render_to_response("observacion/lista.html",ctx,
			context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_add_observacion(request):
	if request.method == "POST":
		form  = observacionForm(request.POST)
		if form.is_valid():
			o = form.save(commit=False)
			o.activo = True
			o.save()
			return HttpResponseRedirect("/observacion/")
		else:
			form  = observacionForm(request.POST)
			ctx = {'form':form}
			return render_to_response('observacion/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = observacionForm()
		ctx = {'form':form}
		return render_to_response('observacion/add.html',ctx,
					context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_editar_observacion(request,id):
	try:
		o = observacion.objects.get(pk=id)
		if request.method == "POST":
			form  = observacionForm(request.POST,instance=o)
			if form.is_valid():
				o = form.save(commit=False)
				o.activo = True
				o.save()
				return HttpResponseRedirect("/observacion/")
			else:
				form  = observacionForm(request.POST)
				ctx = {'form':form}
				return render_to_response('observacion/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = observacionForm(instance=o)
			ctx = {'form':form}
			return render_to_response('observacion/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el observacion solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

