from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import RegistrationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'main/home.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main')
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
