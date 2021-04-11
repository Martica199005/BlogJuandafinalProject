from django.shortcuts import render,redirect
from .models import Articles, Comment
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib import messages
#from django.http import HttpResponse
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.http import HttpResponse


@login_required(login_url="/accounts/login")
def articles_list(request):
  articles= Articles.objects.all().order_by('date')
  template='articles/articles_list.html'
  return render(request,template, {'articles':articles})



def articles_details(request,slug): 
  #return HttpResponse(slug)
  articles=Articles.objects.get(slug=slug)
  return render(request,'articles/articles_details.html',{'articles':articles})

#@login_required(login_url="/accounts/login")
def article_create(request):
  if request.method=="POST":
    form=forms.CreateArticles(request.POST, request.FILES)
    if form.is_valid():
      #save article to db
      istance=form.save(commit=False)
      istance.author=request.user
      istance.save()
      return redirect('articles:list')
  else:
    form=forms.CreateArticles()
  return render(request,'articles/article_create.html', {'form':form})

def delete_article(request,slug):
  print(slug)
  Articles.objects.get(slug=slug).delete()
  return redirect('articles:list')

def like_article(request,slug):
  articles=Articles.objects.get(slug=slug)
  articles.likes.add(request.user)
  return redirect('articles:list')

def article_subject(request):
  articles= Articles.objects.all().order_by('date')
  subject="workout"
  articles= articles.filter(subject__icontains=subject)
  return render(request,'articles/articles_subject.html',{'articles':articles})


def articles_nutrition(request):
  articles= Articles.objects.all().order_by('date')
  subject="nutrition"
  articles= articles.filter(subject__icontains=subject)
  return render(request,'articles/articles_nutrition.html',{'articles':articles})


def articles_massages(request):
  articles= Articles.objects.all().order_by('date')
  subject="massages"
  articles= articles.filter(subject__icontains=subject)
  return render(request,'articles/articles_massages.html', {'articles':articles})


def articles_massages(request):
  articles= Articles.objects.all().order_by('date')
  subject="massages"
  articles= articles.filter(subject__icontains=subject)
  return render(request,'articles/articles_massages.html', {'articles':articles})

def edit_article(request,slug):
    article = Articles.objects.get(slug=slug) 
    if request.method == 'POST':
        form = forms.EditArticle(request.POST, instance=article)
        if form.is_valid():
          form.save()
          return redirect('articles:list')
    else:
         form = forms.EditArticle(instance=article)
    args = {'form': form}
    return render(request, 'articles/edit_article.html', args)



#Implement comment adding feature
def add_comment(request,slug):
  articles=Articles.objects.get(slug=slug)
  if request.method=="POST":
    inputtxt=request.POST.get("getrow")
    #print(inputtxt)
    comment=Comment.objects.create(article=articles,name=request.user,body=inputtxt)
    return redirect('articles:list')










  











  

  









