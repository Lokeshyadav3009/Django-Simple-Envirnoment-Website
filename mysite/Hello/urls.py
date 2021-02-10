from django.contrib import admin
from django.urls import path,include
from Hello import views

urlpatterns = [
    path("home/",views.homep,name="home"),
    path("reg/",views.reg,name="reg"),
    path("result/",views.result,name="result"),
]
