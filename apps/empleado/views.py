from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import empleado
from .forms import empleadoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def view_lista_empleados(request):
	form = empleadoForm()
	lista = empleado.objects.filter(activo=True)
	ctx = {'lista':lista,'form':form}
	return render_to_response("empleado/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_empleado(request,id):
	try:
		e = empleado.objects.get(pk=id)
		U = User.objects.get(pk=e.empleado.id)
		if request.method == "POST":
			form_empleado  = empleadoForm(request.POST,instance=e)
			if form_empleado.is_valid():
				emp = form_empleado.save(commit=False)
                                emp.empleado = U
				emp.save()
				U.first_name = str(request.POST['nombre'])
				U.last_name = str(request.POST['apellidos'])
				U.save()
				return HttpResponseRedirect("/empleado/")
			else:
				form_user  = empleadoForm(request.POST)
				form_empleado  = userForm(request.POST)
				ctx = {'form_user':form_user,'form_empleado':form_empleado}
				return render_to_response('empleado/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			ctx_user = {'nombre':U.first_name,'apellidos':U.last_name}
			form_empleado = empleadoForm(instance=e,initial=ctx_user)
			ctx = {'form_empleado':form_empleado}
			return render_to_response('empleado/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
					
					
def view_agregar_empleado(request,id):
	try:
		U = User.objects.get(pk=id)
		if request.method == "POST":
			form  = empleadoForm(request.POST)
			if form.is_valid():
				emp = form.save(commit=False)
				emp.empleado = U
				emp.save()
				U.first_name=request.POST['nombre']
				U.last_name=request.POST['apellidos']
				U.is_staff = True
				U.save()
				return HttpResponseRedirect("/empleado/")
			else:
				form  = empleadoForm(request.POST)
				ctx = {'form':form}
				return render_to_response('empleado/add.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = empleadoForm()
			ctx = {'form':form}
			return render_to_response('empleado/add.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
		ctx = {'msg':"No se encontro el perfil solicitado"}
		return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
def view_add_user(request):
	if request.method == "POST":
		form  = UserCreationForm(request.POST)
		if form.is_valid():
			U = form.save()
			return HttpResponseRedirect("/empleado/%i/agregar/"% U.id)
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


