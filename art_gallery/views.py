from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Category, Image

# Create your views here.
def home(request):
    title = 'Home is working'
    images = Image.objects.all()
    categories = Category.objects.all()
    context={
        'categories':categories,
        'title': title,
        'images' : images,
    }
    return render(request, 'home.html', context)
