from typing import Any
from django import http
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from django.http import JsonResponse
from django.forms import modelformset_factory
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

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

# def get_name_by_id(request, slug):
#     split_slug = slug.split('-')
#     # return HttpResponse(f"Эта страница под id { ' '.join(slug.split('-'))}")
#     return render(request, 'Telegraph.html')
    
class get_name_by_id(TemplateView):
    template_name = 'tele/Telegraph.html'
    
    def post(self, request, *args: Any, **kwargs: Any) -> HttpResponse:
        print(args, kwargs)
        return super().post(request, *args, **kwargs)
        
    

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

    

class ArticleCreate(CreateView):
    model = Article
    fields = ['name','msg','img']
    template_name = "tele/CreateArticle.html"
    
    
class ShowArticle(DetailView):
    # pk_url_kwarg = "title"
    model = Article
    template_name = "tele/ShowArticle.html"
    
    def get_context_data(self, **kwargs):
        context = super(ShowArticle, self).get_context_data(**kwargs)
        
        context['article'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['imgs'] = Images.objects.all().filter(post = self.kwargs['pk']) 
        
        return context
    
@csrf_exempt
def check(request):
    # print(request)

    return JsonResponse({"short_name":"","author_name":"","author_url":"","save_hash":"ee09c197b42b76500c1af90a14fc24bb90a9","can_edit":False})

def post(request):
 
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
        
        print(request.POST)
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    
    
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.save()
    
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect(f"/{post_form.pk}")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'tele/index.html',
                  {'postForm': postForm, 'formset': formset})
    
    

        