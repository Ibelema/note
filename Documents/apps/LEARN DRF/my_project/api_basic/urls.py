from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails

urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),#class based views
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view()),
]