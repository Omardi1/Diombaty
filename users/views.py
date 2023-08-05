from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

@login_required(login_url="/login")
def sign_up (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = RegisterForm()
    return render(request, 'register/sign_up.html', {"form": form})    
