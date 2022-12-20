from django.urls import path
from . import views

app_name = 'posts'

urlpatterns= [
    #Homepage
    path('', views.homepage, name='homepage'),
]
