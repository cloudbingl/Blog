from django.urls import path
from . import views

app_name = 'favour'

urlpatterns = [
    path('obj/', views.favour_changed, name='favour'),
]
