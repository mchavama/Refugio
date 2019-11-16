from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def idx_adopcion(request):
    return HttpResponse("I am the main page of the app Adopcion")