from django.shortcuts import render

# Create your views here.
def index(request): return render(request ,'abc/index.html')
def contact(request): return render(request ,'abc/contactus.html')
