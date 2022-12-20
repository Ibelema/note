from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout


# Create your views here.
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts:homepage'))
