from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm, LoginUserForm
from django.shortcuts import render, redirect


def register_view(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('products')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')

    context = {'form': form}
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
