from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import empleado
from .forms import empleadoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.alumno.forms import nombreYpellidoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_del_empleado(request,id):
	try:
		e = empleado.objects.get(pk=id)
		e.activo = False
		e.save()
		return HttpResponseRedirect('/empleado/')
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el empleado solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_lista_empleados(request):
	contact_list =empleado.objects.order_by('id').reverse()
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
	return render_to_response("empleado/lista.html",ctx,
			context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_editar_empleado(request,id):
	try:
		e = empleado.objects.get(pk=id)
		U = User.objects.get(pk=e.empleado.id)
		if request.method == "POST":
			form_empleado  = empleadoForm(request.POST,request.FILES,instance=e)
			if form_empleado.is_valid():
				emp = form_empleado.save(commit=False)
				emp.empleado = U
				emp.save()
				U.first_name = str(request.POST['nombre'])
				U.last_name = str(request.POST['apellidos'])
				U.save()
				return HttpResponseRedirect("/empleado/")
			else:
				form_datos = nombreYpellidoForm(request.POST)
				form_empleado  = empleadoForm(request.POST,request.FILES)
				ctx = {'form_empleado':form_empleado,'form_datos':form_datos}
				return render_to_response('empleado/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			ctx_user = {'nombre':U.first_name,'apellidos':U.last_name}
			form_datos = nombreYpellidoForm(initial=ctx_user)
			form_empleado = empleadoForm(instance=e)
			ctx = {'form_empleado':form_empleado,'form_datos':form_datos}
			return render_to_response('empleado/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el empleado solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_add_user(request):
	if request.method == "POST":
		form  = UserCreationForm(request.POST)
		if form.is_valid():
			U = form.save(commit=False)
			U.first_name = U.username
			U.save()
			E = empleado(empleado=U)
			E.save()
			
			return HttpResponseRedirect("/empleado/%i/editar/"% E.id)
		else:
			form  = UserCreationForm(request.POST)
			ctx = {'form':form}
			return render_to_response('empleado/user.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = UserCreationForm()
		ctx = {'form':form}
		return render_to_response('empleado/user.html',ctx,
				context_instance=RequestContext(request))


