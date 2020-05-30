from django.shortcuts import render,redirect
from .models import Articles
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site





def articles_list(request):
  articles= Articles.objects.all().order_by('date')

  return render(request,'articles/articles_list.html', {'articles':articles})



def articles_details(request,slug):
  #return HttpResponse(slug)
  articles=Articles.objects.get(slug=slug)
  current_site = get_current_site(request)
  print("current site:")
  if current_site.domain == 'blogjuanda1.herokuapp.com':
        print("blogjuanda1.herokuapp.com")
        current_site="https://"+str(current_site)
  else:
        print(current_site.domain)
        current_site="http://"+str(current_site)
  return render(request,'articles/articles_details.html',{'articles':articles, 'current_site':current_site})

@login_required(login_url="/accounts/login")
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

def article_workout(request):
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


def massages(request):
  return render(request,'articles/massages_services.html')

def coaching(request):
  return render(request,'articles/coaching_services.html')




  
  








  

  









