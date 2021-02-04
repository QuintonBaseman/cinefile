from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'user_accounts/home.html')

def search(request):
    return render(request, 'user_accounts/search.html')

def userHomePage(request):
    if request.user.is_authenticated:
        return render(request, 'user_accounts/user_home.html')
    else:
        return render(request, 'user_accounts/not_allowed.html')


def signupPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context = {'form':form}
    return render(request, 'user_accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "user_accounts/login.html",
                    context={"form":form})

def movieDetail(request):
    return render(request, 'user_accounts/movie_detail.html')
