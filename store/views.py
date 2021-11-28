from django.shortcuts import render, redirect
from .models import Product
from django.conf import settings

def homepage(request):
    context = {'products': Product.objects.all()}
    return render(request, 'store/homepage.html', context)

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'store/checkout.html')
