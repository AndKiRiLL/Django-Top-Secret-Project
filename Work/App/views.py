from django.shortcuts import render, redirect
from .forms import FormAdd, FilmsEditForm
from .models import *
from django.http import HttpResponseRedirect, HttpResponseNotFound

def index(request):
    films = Films.objects.all()
    return render(request, 'index.html', {'films': films})

def edit_choose(request, id):
    try:
        if request.method == "POST":
            film = Films.objects.get(id=id)

            film.name = request.POST.get('name', 'Undefined')
            film.category = request.POST.get('category', 'Undefined')
            film.date_create = request.POST.get('date_create', 'Undefined')
            film.actors = request.POST.get('actors', 'Undefined')
            film.date_visible = request.POST.get('date_visible', 'Undefined')

            film.save()

            films = Films.objects.all()
            return render(request, 'edit.html', context={'films': films})

        else:
            film = Films.objects.get(id=id)
            form = FilmsEditForm(instance=film)
            return render(request, 'edit_choose.html', context={'form': form})

    except Films.DoesNotExist:
        return HttpResponseRedirect('/')


def edit(request):
    films = Films.objects.all()
    return render(request, 'edit.html', {'films': films})

def delete(request):
    films = Films.objects.all()
    return render(request, 'delete.html', {'films': films})

def delete_choose(request, id):
    try:
        films = Films.objects.get(id=id)
        films.delete()
        films = Films.objects.all()
        return render(request, 'delete.html', {'films': films})
    except Films.DoesNotExist:
        films = Films.objects.all()
        return render(request, 'delete.html', {'films': films})



def add(request):
    if request.method == "POST":

        name = request.POST.get('name', 'Undefined')
        category = request.POST.get('category', 'Undefined')
        date_create = request.POST.get('date_create', 'Undefined')
        actors = request.POST.get('actors', 'Undefined')
        date_visible = request.POST.get('date_visible', 'Undefined')

        Films.objects.create(name=name, category=category, date_create=date_create, actors=actors, date_visible=date_visible)
        return HttpResponseRedirect('/')

    else:
        form_add = FormAdd()
        return render(request, 'add.html', context={'form_add': form_add})
