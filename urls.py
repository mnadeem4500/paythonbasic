from django.contrib import admin
from django.urls import path
from . import views
from . import calculate

urlpatterns = [
    path("", views.index, name="index"),
    path("calculate/", calculate.cel, name="calculate"),
    path("Gender/", views.Gender, name="Gender"),
    path


]