from django.contrib import admin
from django.urls import path,include
from Hello import views

urlpatterns = [
    path("",views.firstfunc,name="home")
]
