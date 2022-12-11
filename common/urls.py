from django.urls import path

from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('resorts',views.resorts,name='resorts'),
    path('entertaiments',views.entertaiments,name='entertaiments'),




]