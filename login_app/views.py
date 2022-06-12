from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages

@login_required
def home(request):
    return render(request, 'login_pages/home.html')

def join_us(request):
    if request.user.is_authenticated:
        messages.success(request, "You're already logged-in!")
        return redirect('/')
    signup_form = CreateUserForm()
    if request.method == 'POST':
        signup_form = CreateUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successful')
            return redirect('/join-us')
    
    context = {'signup_form': signup_form}
    return render(request, 'login_pages/join_us.html', context)

def login_user(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged-in!')
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('/')
        else:
            messages.success(request, 'Username or password is incorrect')
            return redirect('/join-us/')

@login_required        
def logout_user(request):
    logout(request)
    return redirect('/join-us/')
    
def reset_password(request):
    return render(request, 'login_pages/reset_password.html')

def reset_email_sent(request):
    return render(request, 'login_pages/reset_email_sent.html')