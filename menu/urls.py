from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('sub_menu/<str:name>', views.Menu.as_view(), name="menu"),
]
