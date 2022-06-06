from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import RegistrationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import logging
import asyncio
from asgiref.sync import sync_to_async
logger = logging.getLogger(__name__)


@sync_to_async
def home(request):
    logger.info("Home page!")
    return render(request, 'main/home.html')


def register(request):
    logger.info("Registering page!")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Registered!")
            return redirect('/main')
        else:
            logger.error("Not valid registration form!")
    else:
        form = RegistrationForm()

        # args = {'form': form}
    return render(request, 'main/reg_form.html', {'form': form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/main')
        else:
            return redirect('/main/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'main/change_password.html', {'form': form})