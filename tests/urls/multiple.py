from django.shortcuts import render
from django.urls import path

urlpatterns = [
    path("multiple/", render, name="multiple-direct"),
]
