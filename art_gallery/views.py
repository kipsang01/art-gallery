from django.shortcuts import render
from django.http  import HttpResponse, Http404

# Create your views here.
def home(request):
    title = 'Home is working'
    context={
        'title': title,
    }
    return render(request, 'home.html', context)
