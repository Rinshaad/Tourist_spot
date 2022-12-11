from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def gallery(request):
    return render(request, 'gallery.html')
def about(request):
    return render(request, 'about.html')
def resorts(request):
    return render(request, 'resorts.html')
def entertaiments(request):
    return render(request, 'entertaiments.html')