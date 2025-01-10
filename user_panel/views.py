from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import SignUpForm

from django.contrib.auth import logout




# @login_required
# def logout_view(request):
#     return render(request, 'registration/logout.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(request.method)
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}')
            print('signup succ')
            return redirect('pages:home')  # Replace 'home' with your home page URL name
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def custom_logout_view(request):
    logout(request)  # Ends the session
    return redirect("pages:home")  # Redirect to the desired page after logout

from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('pages:home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {})


# def authView(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'registration/login.html')
#     else:
#         form  = UserCreationForm()
        
#     return render(request, 'registration/signup.html' , {'form': form})