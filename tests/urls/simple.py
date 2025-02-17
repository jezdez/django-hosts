from django.shortcuts import render
from django.urls import path

urlpatterns = [
    path("simple/", render, name="simple-direct"),
]
