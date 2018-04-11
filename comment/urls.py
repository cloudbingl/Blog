from django.urls import path

from . import views

app_name = 'comment'

urlpatterns = [
    path('add_comment/', views.add_comment, name='add_comment'),
]