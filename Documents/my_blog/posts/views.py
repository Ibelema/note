from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article
# Create your views here.

#to show homepage
def homepage(request):
    return render(request, 'posts/homepage.html')

#to show all posts we do this
def posts(request):
    posts = Article.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'posts/posts.html')
