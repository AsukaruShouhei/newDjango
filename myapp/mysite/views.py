from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sample(request):
    return render(request, 'mysite/index.html')
    # return HttpResponse("Hello, world. You're at the polls sample.")
