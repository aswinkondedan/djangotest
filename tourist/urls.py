
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.homefunction,name='home'),
    path('about',views.aboutfunction,name='about'),
    
    
]
