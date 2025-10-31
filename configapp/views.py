from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    news = News.objects.all()
    category = Category.objects.all()
    content ={
        "news":news,
        "category":category
    }
    return render(request, 'index.html', content)

def category(request):
    category = Category.objects.all()
    content = {
        "category": category
    }
    return render(request, 'category.html', content)
