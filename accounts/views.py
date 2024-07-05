from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import register_form,CustomPasswordChangeForm

def index(request):
    return render(request, 'accounts/home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in...")
            return redirect(next_url or 'home')
        messages.error(request, "Wrong User Name or Password")
    return render(request, 'accounts/login.html')

def user_register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            # user_form.set_password(request.POST['password'])
            user_form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully registered and Logged in...")
                return redirect('home')
            messages.error(request, "Some Error Occured so not logged in...")
            return render(request, 'accounts/register.html')
        return render(request, 'accounts/register.html', {'form': form})
    return render(request, 'accounts/register.html')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request,'Your Session Has been terminated...')
    return redirect('login_user')

@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully...")
            return redirect('home')
        else:
            return render(request, 'accounts/change_password.html', {'form': form})
    return render(request, 'accounts/change_password.html')

