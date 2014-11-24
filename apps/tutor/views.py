from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.tutor.models import tutor
from .forms import tutorForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from iicea.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def view_add_tutor(request):
	if request.method == "POST":
		form  = tutorForm(request.POST)
		if form.is_valid():
			t = form.save(commit=False)
			t.activo =True
			t.save()
			return HttpResponseRedirect("/tutor/")
		else:
			form  = tutorForm(request.POST)
			ctx = {'form':form}
			return render_to_response('tutor/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = tutorForm()
		ctx = {'form':form}
		return render_to_response('tutor/add.html',ctx,
				context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_lista_tutores(request):
	contact_list = tutor.objects.order_by('id').reverse()
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
	return render_to_response("tutor/lista.html",ctx,
			context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def view_editar_tutor(request,id):
	try:
		t = tutor.objects.get(pk=id)
		if request.method == "POST":
			form  = tutorForm(request.POST,instance=t)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/tutor/")
			else:
				form  = tutorForm(request.POST)
				ctx = {'form':form}
				return render_to_response('tutor/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = tutorForm(instance=t)
			ctx = {'form':form}
			return render_to_response('tutor/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el perfil solicitado"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def view_del_tutor(request,id):
	t = tutor.objects.get(pk=id)
	t.activo = False
	t.save()
	return HttpResponseRedirect('/tutor/')
	
