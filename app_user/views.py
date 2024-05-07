from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app_user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from app_user.models import User, EmailVerification


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


@login_required(login_url='user_app:login')
def logout_view(request):
    auth.logout(request)
    messages.info(request, 'Вы вышли из аккаунта!')
    return HttpResponseRedirect(reverse('app_home:home'))


@login_required(login_url='user_app:login')
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
    return render(request, 'app_user/register.html', context=context)
