from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracker/', views.tracker, name='tracker'),
    path('credits/', views.credits, name='credits'),
]