from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    #Login Page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    
    #Logout page
    path('logout/', LogoutView.as_view(), name='logout'),

]