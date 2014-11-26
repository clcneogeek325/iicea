from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import concepto_pago
from .forms import concepto_pagoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_lista_concepto_pagos(request):
	contact_list = concepto_pago.objects.order_by('id').reverse()
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
	return render_to_response("concepto_pago/lista.html",ctx,
			context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_add_concepto_pago(request):
	if request.method == "POST":
		form  = concepto_pagoForm(request.POST)
		if form.is_valid():
			cp = form.save(commit=False)
			cp.activo = True
			cp.save()
			return HttpResponseRedirect("/concepto_pago/")
		else:
			form  = concepto_pagoForm(request.POST)
			ctx = {'form':form}
			return render_to_response('concepto_pago/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = concepto_pagoForm()
		ctx = {'form':form}
		return render_to_response('concepto_pago/add.html',ctx,
				context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_editar_concepto_pago(request,id):
	try:
		cp = concepto_pago.objects.get(pk=id)
		if request.method == "POST":
			form  = concepto_pagoForm(request.POST,instance=cp)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/concepto_pago/")
			else:
				form  = concepto_pagoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('concepto_pago/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = concepto_pagoForm(instance=cp)
			ctx = {'form':form}
			return render_to_response('concepto_pago/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el concepto de pago solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_del_concepto_pago(request,id):
	try:
		cp = concepto_pago.objects.get(pk=id)
		cp.activo = False
		cp.save()
		return HttpResponseRedirect('/concepto_pago/')
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el concepto de pago solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
