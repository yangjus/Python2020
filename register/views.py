from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("store-homepage")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})

def login(response):
    return render(response, "registration/login.html")

def logout_site(request):
    print('logged out')
    logout(request)
    return redirect('store-homepage')
