from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

from .forms import *


def pageNotFound(exeption):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def pageNotFoundd(request, exeption):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')    
    
    
class ShowArticle(DetailView):
    # pk_url_kwarg = "title"
    model = Article
    template_name = "tele/showArticle.html"
    
    def get_context_data(self, **kwargs):
        context = super(ShowArticle, self).get_context_data(**kwargs)
        
        context['article'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['imgs'] = Images.objects.all().filter(post = self.kwargs['pk']) 
        
        return context
    

def CreateArticle(request):
 
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
        
        imgs = request.FILES.getlist('pro-image')
        # imgss = request.FILES.getlist('pro-image')
        
        print(request.FILES.getlist('pro-image'))
        print(imgs)
        postForm = PostForm(request.POST)
    
    
        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.save()
            
            for image in imgs:
                Images.objects.create(
                    post = post_form,
                    image = image
                )

            return HttpResponseRedirect(f"/{post_form.pk}")
    else:
        postForm = PostForm()
    return render(request, 'tele/index.html',
                  {'postForm': postForm})
    