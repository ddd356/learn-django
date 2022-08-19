from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request, name = "ind"):
    return HttpResponse(f"Hello, world. You're at the polls index. {name}")
