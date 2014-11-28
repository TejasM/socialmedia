from dashboard.models import UserProfile, UserSpec
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import DataError
from django.shortcuts import render, redirect

__author__ = 'tmehta'


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                return redirect(reverse('dashboard:main'))
            else:
                pass
        else:
            return redirect(reverse('dashboard:login'))
    else:
        if request.user.is_authenticated():
            return redirect(reverse('dashboard:main'))
        return render(request, 'dashboard/login.html')


def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        company_name = request.POST.get('company_name', '')
        try:
            user = User.objects.create(username=username, email=username, first_name=first_name, last_name=last_name)
        except DataError:
            return redirect(reverse('dashboard:signup'))
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, company_name=company_name)
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                return redirect(reverse('dashboard:main'))
            else:
                pass
        else:
            return redirect(reverse('dashboard:signup'))
    else:
        if request.user.is_authenticated():
            return redirect(reverse('dashboard:main'))
        return render(request, 'dashboard/sign_up.html')


def main(request):
    if request.method == "POST":
        pass
    else:
        specs = UserSpec.objects.filter(user=request.user)
        return render(request, 'dashboard/index.html', {'specs': specs})


def create_spec(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'dashboard/create_spec.html')


def edit_spec(request, spec_id):
    if request.method == "POST":
        pass
    else:
        spec = UserSpec.objects.get(pk=spec_id)
        return render(request, 'dashboard/edit_spec.html', {'spec': spec})