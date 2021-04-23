from django.shortcuts import render, redirect
from .models import Item

# Create your views here.

def index(request):
  items = Item.objects.all()
  return render(request, 'index.html', {'items': items})