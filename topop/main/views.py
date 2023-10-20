from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def run_index(request):

    return render(request, 'index.html')


def index():
    pass


def run_codes_page(request):
    return render(request, 'Codeshop.html')


def contactus(request):
    return render(request, 'Contact.html')


def news(request):
    return render(request, 'News.html')


def Login_Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect("Home")
        else:
            messages.success(request, "There was a problem in logging in")
            return redirect("LoginSignup")
    else:
        return render(request, 'LoginSignup.html')


def log_out(request):
    logout(request)
    messages.success(request, "You successfully Logged out!")
    return redirect("Home")


def register(request):
    if request.method == "POST":
        username = request.POST.get('regusername')
        password = request.POST.get('regpassword')
        email = request.POST.get('regemail')

        if username and password and email:
            try:
                User.objects.create_user(username=username, password=password, email=email)
                messages.success(request, "Registration successful!")
                return redirect("LoginSignup")  # Redirect to the login page
            except Exception as ex:
                messages.error(request, f"Registration failed. Error: {str(ex)}")
        else:
            messages.error(request, "Invalid form data. Please try again.")
    return render(request, 'LoginSignup.html')


def forgot_password(request):
    return render(request, 'ForgotPassword.html')


def password_reset(request):
    if request.method == "POST":
        password_form = PasswordResetForm(request.POST)
    else:
        password_form = PasswordResetForm()
    context = ({
        "password_form": password_form,
    })
    return render(request, 'ResetPassword.html', context)


def reset_password_done(request):
    render(request, 'ResetPassword_Done.html')


def forgot_password_done(request):
    render(request, 'ForgetPassword_Done.html')


def product(request):
    pass
