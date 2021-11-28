from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Category, Image

# Create your views here.
def home(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    context={
        'categories':categories,
        'images' : images,
    }
    return render(request, 'home.html', context)


def search_results(request):
    
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        context={
            'images': searched_images,
            'message':message
        }

        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def get_category(request,category):
    images = Image.image_cat(category)
    context={
        'images' : images,
    }
    return render(request, 'category.html', context)