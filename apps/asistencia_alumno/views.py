from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import asistencia_alumno
from .forms import asistencia_alumnoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_eliminar_asistencia_alumno(request,id):
	try:
		aa = asistencia_alumno.objects.get(pk=id)
		aa.activo = False
		aa.save()
		return HttpResponseRedirect('/asistencia_alumno/')
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro la sistencia de alumno solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_lista_asistencia_alumnos(request):
	contact_list = asistencia_alumno.objects.order_by('id').reverse()
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
	return render_to_response("asistencia_alumno/lista.html",ctx,
			context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_editar_asistencia_alumno(request,id):
	try:
		ast = asistencia_alumno.objects.get(pk=id)
		if request.method == "POST":
			form  = asistencia_alumnoForm(request.POST,instance=ast)
			if form.is_valid():
				aa = form.save(commit=False)
				aa.activo=True
				aa.save()
				form.save_m2m()
				return HttpResponseRedirect("/asistencia_alumno/")
			else:
				form  = asistencia_alumnoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('asistencia_alumno/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = asistencia_alumnoForm(instance=ast)
			ctx = {'form':form}
			return render_to_response('asistencia_alumno/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro la sistencia de alumno solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_add_asistencia_alumno(request):
	if request.method == "POST":
		form  = asistencia_alumnoForm(request.POST)
		if form.is_valid():
			a = form.save(commit=False)
			a.activo=True
			a.save()
			form.save_m2m()
			return HttpResponseRedirect("/asistencia_alumno/")
		else:
			form  = asistencia_alumnoForm(request.POST)
			ctx = {'form':form}
			return render_to_response('asistencia_alumno/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = asistencia_alumnoForm()
		ctx = {'form':form}
		return render_to_response('asistencia_alumno/add.html',ctx,
				context_instance=RequestContext(request))

