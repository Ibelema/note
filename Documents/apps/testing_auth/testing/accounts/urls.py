from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signuppage, name='signuppage'),
    path('login/', views.LoginView.as_view(), name='login'),
]