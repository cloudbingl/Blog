from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:pk>/', views.article_detail, name='article')
]