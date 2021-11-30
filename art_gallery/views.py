from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Category, Image,Location

# Create your views here.
def home(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    context={
        'categories':categories,
        'images' : images,
        'locations':locations,
    }
    return render(request, 'home.html', context)

def image_view(request,image_id):
    categories = Category.objects.all()
    try:
        image = Image.get_image_by_id(image_id)
    except Image.DoesNotExist:
            raise Http404()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    context={
        'categories':categories,
        'image' : image,
    }
    return render(request, 'image.html', context)


def search_results(request):
    categories = Category.objects.all()
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        context={
            'categories':categories,
            'images': searched_images,
            'message':message
        }

        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def get_category(request,category):
    categories = Category.objects.all()
    images = Image.image_cat(category)
    context={
        'categories':categories,
        'images' : images,
    }
    return render(request, 'category.html', context)


def get_by_locations(request,location):
    categories = Category.objects.all()
    images = Image.images_by_location(location)
    context={
        'categories':categories,
        'images' : images,
    }
    return render(request, 'category.html', context)