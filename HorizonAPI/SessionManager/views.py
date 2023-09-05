from django.shortcuts import render
from django.http import HttpResponse

def hompage(request):
    return HttpResponse("discipline")