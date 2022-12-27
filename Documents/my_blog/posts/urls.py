from django.urls import path
from . import views

app_name = 'posts'

urlpatterns= [
    #Homepage
    path('', views.homepage, name='homepage'),
    path('posts/', views.posts, name='posts'),
    path('new_post/', views.PostCreate, name='new_post'),
    #Editing posts
    path('edit/', views.EditPost, name='edit'),
]
