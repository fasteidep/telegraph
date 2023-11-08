from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *

# Create your views here.


def adminka(request):
    return redirect('/home')

def home(request):
    return HttpResponse("<h1>Домашняя страница</h1> <p> <a href='/admin' >админка(только для админов)</a>")

def pageNotFound(request,exeption):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            print(request.POST['your_name'])
            print(form.data['your_name'])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        form.fields['selector'].choices = [(i.name,i.name ) for i in Okrug.objects.all()]

        

    return render(request, 'name.html', {'form': form})

def add_okrig(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddOkrug(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            ok = Okrug.objects.create(name=form.data['name'])
            ok.save()
            
            return HttpResponseRedirect('name')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddOkrug()

    return render(request, 'add_okrig.html', {'form': form})