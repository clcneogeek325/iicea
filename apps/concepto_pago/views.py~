from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import concepto_pago
from .forms import concepto_pagoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def view_lista_concepto_pagos(request):
	lista = concepto_pago.objects.all()
	ctx = {'lista':lista}
	return render_to_response("concepto_pago/lista.html",ctx,
			context_instance=RequestContext(request))

def view_add_concepto_pago(request):
	if request.method == "POST":
		form  = concepto_pagoForm(request.POST)
		if form.is_valid():
			form.save()
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
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

