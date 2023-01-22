from django.urls import path
from . import views 


app_name = 'blog'

urlpatterns = [
    path('NewPost/', views.NewPost, name='NewPost'),
    path('post/<int:id>/detail/', views.post_detail, name='post_detail'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:id>/update/', views.update_view, name='update_view'),
    path('post/<int:id>/delete/', views.delete_view, name='delete_view'),
]
