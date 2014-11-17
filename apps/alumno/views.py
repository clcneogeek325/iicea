from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import alumno
from .forms import alumnoForm,nombreYpellidoForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





def view_lista_alumnos(request):
	lista = alumno.objects.filter(activo=True)
	ctx = {'lista':lista}
	return render_to_response("alumno/lista.html",ctx,
			context_instance=RequestContext(request))


def view_editar_alumno(request,id):
	try:
		a = alumno.objects.get(pk=id)
		U = User.objects.get(pk=a.alumno.id)
		print a.alumno.id
		if request.method == "POST":
			form  = alumnoForm(request.POST,instance=a)
			if form.is_valid():
				print "valido"
				alu = form.save(commit=False)
				form.save_m2m()
				alu.alumno = U
				alu.save()
				U.first_name = request.POST['nombre']
				U.last_name = request.POST['apellidos']
				U.save()
				return HttpResponseRedirect("/alumno/")
			else:
				print "no valido",form.errors
				form  = alumnoForm(request.POST)
				form_nom_ape = nombreYpellidoForm(request.POST)
				ctx = {'form_alumno':form,'form_datos':form_nom_ape}
				return render_to_response('alumno/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			ctx_user = {'nombre':U.first_name,'apellidos':U.last_name}
			form_alumno = alumnoForm(instance=a)
			form_nom_ape = nombreYpellidoForm(initial=ctx_user)
			ctx = {'form_alumno':form_alumno,'form_datos':form_nom_ape}
			return render_to_response('alumno/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
		
					
def view_add_user(request):
	if request.method == "POST":
		form  = UserCreationForm(request.POST)
		if form.is_valid():
			U = form.save(commit=False)
			U.first_name = U.username
			U.save()
			A = alumno(alumno=U)
			A.activo = True
			A.save()
			return HttpResponseRedirect("/alumno/%i/editar/"% A.id)
		else:
			form  = UserCreationForm(request.POST)
			ctx = {'form':form}
			return render_to_response('alumno/user.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = UserCreationForm()
		ctx = {'form':form}
		return render_to_response('alumno/user.html',ctx,
				context_instance=RequestContext(request))


