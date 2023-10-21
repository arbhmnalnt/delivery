from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    departments = Department.objects.all()

    ctx = {'deps':departments}
    return render(request, 'website/index.html', ctx)