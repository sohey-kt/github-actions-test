from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def App_view(request):
    return HttpResponse('Hello world!')
