from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import materia
from .forms import materiaForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def view_lista_materias(request):
	contact_list = materia.objects.order_by('id').reverse()
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
	return render_to_response("materia/lista.html",ctx,
			context_instance=RequestContext(request))

def view_add_materia(request):
	if request.method == "POST":
		form  = materiaForm(request.POST)
		if form.is_valid():
			m = form.save(commit=False)
			m.activo  = True
			m.save()
			return HttpResponseRedirect("/materia/")
		else:
			form  = materiaForm(request.POST)
			ctx = {'form':form}
			return render_to_response('materia/add.html',ctx,
					context_instance=RequestContext(request))	
	else:
		form = materiaForm()
		ctx = {'form':form}
		return render_to_response('materia/add.html',ctx,
				context_instance=RequestContext(request))

def view_editar_materia(request,id):
	try:
		m = materia.objects.get(pk=id)
		if request.method == "POST":
			form  = materiaForm(request.POST,instance=m)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/materia/")
			else:
				form  = materiaForm(request.POST)
				ctx = {'form':form}
				return render_to_response('materia/edit.html',ctx,
						context_instance=RequestContext(request))	
		else:
			form = materiaForm(instance=m)
			ctx = {'form':form}
			return render_to_response('materia/edit.html',ctx,
					context_instance=RequestContext(request))
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el materia solicitada"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))

def view_del_materia(request,id):
	try:
		m = materia.objects.get(pk=id)
		m.activo = False
		m.save()
		return HttpResponseRedirect('/materia/')
	except ObjectDoesNotExist:
			ctx = {'msg':"No se encontro el materia solicitada"}
			return render_to_response('msg.html',ctx,
					context_instance=RequestContext(request))
