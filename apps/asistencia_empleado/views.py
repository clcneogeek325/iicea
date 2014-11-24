from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import asistencia_empleado
from .forms import asistencia_empleadoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_eliminar_asistencia_empleado(request,id):
	ae = asistencia_empleado.objects.get(pk=id)
	ae.activo = False
	ae.save()
	return HttpResponseRedirect('/asistencia_empleado/')

@login_required(login_url=URL_LOGIN)
def view_lista_asistencia_empleados(request):
	contact_list = asistencia_empleado.objects.order_by('id').reverse()
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
	return render_to_response("asistencia_empleado/lista.html",ctx,
			context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_editar_asistencia_empleado(request,id):
	try:
		ast = asistencia_empleado.objects.get(pk=id)
		if request.method == "POST":
			form  = asistencia_empleadoForm(request.POST,instance=ast)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/asistencia_empleado/")
			else:
				form  = asistencia_empleadoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('asistencia_empleado/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = asistencia_empleadoForm(instance=ast)
			ctx = {'form':form}
			return render_to_response('asistencia_empleado/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_add_asistencia_empleado(request):
	if request.method == "POST":
		form  = asistencia_empleadoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/asistencia_empleado/")
		else:
			form  = asistencia_empleadoForm(request.POST)
			ctx = {'form':form}
			return render_to_response('asistencia_empleado/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = asistencia_empleadoForm()
		ctx = {'form':form}
		return render_to_response('asistencia_empleado/add.html',ctx,
				context_instance=RequestContext(request))

