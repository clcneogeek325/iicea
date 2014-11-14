from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http  import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm




@login_required(login_url='/login/')
def view_index(request):
	return render_to_response('index.html',
			context_instance=RequestContext(request))

def view_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

def view_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if user.is_staff or user.is_superuser:
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/lista_semestres/')
			else:
				msg = "El usuario esta inhabilitado usted necesita ponerse en contacto con el administrador(a)"
				ctx = {'msg':msg}
				return render_to_response('error.html',ctx,
					context_instance=RequestContext(request))
		else:
			# Sus usuario y contrasenia son incorrectos
			msg = "LA contrasenia y el usuario son incorrectos"
			ctx = {'msg':msg}
			return render_to_response('error.html',ctx,
				context_instance=RequestContext(request))
	else:
		form = AuthenticationForm()
		ctx = {'form':form}
		return render_to_response('login.html',ctx,
			context_instance=RequestContext(request))

