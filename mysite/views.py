from django.shortcuts import render
import datetime

def my_homepage_view(request):
    now = datetime.datetime.now()
    return render(request, 'base.html', {'current_date': now})
