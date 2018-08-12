from django.shortcuts import render
from django.http import HttpResponse
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sample(request):
    i = {'conte': BASE_DIR}
    return render(request, 'mysite/index.html', i)

def chat(request):
    content = request
    return render(request, 'index.html', content)