from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EmailChangeForm
from django.contrib import messages

from app_user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from app_user.models import User, EmailVerification
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    context = {
        'title': 'Авторизация',
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('app_user:profile'))
        else:
            messages.error(request, 'Неправильные имя или пароль', extra_tags='danger')
    else:
        if request.user.is_authenticated:
            print('request.user.is_authenticated')
            # return HttpResponseRedirect(reverse('app_user:profile'))
        else:
            form = UserLoginForm()
    context['form'] = UserLoginForm()
    return render(request, 'app_user/login.html', context)


@login_required(login_url='app_user:login')
def logout_view(request):
    auth.logout(request)
    messages.info(request, 'Вы вышли из аккаунта!')
    return HttpResponseRedirect(reverse('app_home:home'))


@login_required(login_url='app_user:login')
def profile_view(request):
    username = request.user.username
    context = {
        'title': f'{username} - Профиль пользователя',
    }
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль успешно обновлен!', extra_tags='success')
            return HttpResponseRedirect(reverse('app_user:profile'))
        else:
            messages.error(request, 'При обновлении профиля произошла ошибка!', extra_tags='danger')
    else:
        form = UserProfileForm(instance=request.user)
    context['form'] = form
    return render(request, 'app_user/profile.html', context=context)


def email_verification(request, email, code):
    context = {
        'title': 'Подтверждение почты',
    }
    user = User.objects.get(email=email)
    user_email_verification = EmailVerification.objects.filter(user=user, code=code)
    if user_email_verification.exists():
        user.verified_email = True
        user.save()
        messages.success(request, 'Ваша почта успешно подтверждена!', extra_tags='success')
        return render(request, 'app_user/email_verification.html', context=context)
    else:
        messages.error(request, 'Код подтверждения некорректен!', extra_tags='danger')
    return HttpResponseRedirect(reverse('app_user:profile'))


def register_view(request):
    context = {
        'title': 'Регистрация',
        'form': UserRegistrationForm(),
    }
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app_home:home')
        else:
            context['message_error'] = form.errors
    else:
        form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'app_user/register.html', context=context)


@login_required(login_url='app_user:login')
def change_password(request):
    context = {
        'title': 'Смена пароля',
    }
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Пароль успешно изменен.')
            return redirect('app_user:profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки ниже.')
    else:
        form = PasswordChangeForm(request.user)
    context['form'] = form
    return render(request, 'app_user/change_password.html', context=context)


@login_required(login_url='app_user:login')
def user_delete(request):
    if request.method == 'POST':
        request.user.is_active = False
        request.user.save()
        auth.logout(request)
        messages.info(request, 'Аккаунт удален. Спасибо за пользование нашего сайта!', extra_tags='success')
        return redirect('app_home:home')
    return render(request, 'app_user/user_delete.html')


@login_required(login_url='app_user:login')
def change_email(request):
    context = {
        'title': 'Смена почты',
    }
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email успешно изменен.')
            return redirect('change_email')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки ниже.')
    else:
        form = EmailChangeForm(instance=request.user)
    context['form'] = form
    return render(request, 'app_user/change_email.html', context=context)

