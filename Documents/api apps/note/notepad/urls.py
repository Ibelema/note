from django.urls import path
from .views import notebook_list, notebook_detail

urlpatterns = [
    path('notebook/', notebook_list),
    path('detail/<int:pk>/', notebook_detail),
]