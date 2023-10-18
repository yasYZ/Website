from django.shortcuts import render
from .models import login_account
from django.contrib.auth import authenticate, login, logout



def run_index(request):
    return render(request, 'index.html')


def Login_Register(request):
    if request.method == "POST":
        username = request.POST('loginemail')
        password = request.POST('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        

