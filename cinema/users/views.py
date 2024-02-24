from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.urls import reverse
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = CustomUser(name=name, username=username, email=email, password=password, role=role)
        user.save()

        return redirect('users/login')  # Перенаправление на страницу входа после успешной регистрации

    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    if request.method == 'GET':
        logout(request)

        # После выхода из системы, перенаправляем пользователя на главную страницу
        return redirect(reverse('index'))  # Используем имя URL 'index', определенное в main.urls
    else:
        # Обработка других методов, если необходимо
        # Например, вернуть ошибку метода недопустимого запроса
        return HttpResponseNotAllowed(['GET'])