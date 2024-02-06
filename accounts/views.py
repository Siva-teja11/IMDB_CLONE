# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def register(request):
    registered = False
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Change 'home' to your home page URL
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        user_form = LoginForm()
    return render(request, 'login.html', {'user_form':user_form})

