from django.shortcuts import render
import datetime

def my_homepage_view(request):
    return render(request, 'index.html')

def about_me_view(request):
    return render(request, 'about.html')
