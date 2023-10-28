from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from topop.settings import EMAIL_HOST_USER
from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

def run_index(request):
    return render(request, 'En/index.html')


def index():
    pass


def run_codes_page(request):
    return render(request, 'En/Codeshop.html')


def contactus(request):
    return render(request, 'En/Contact.html')


def news(request):
    return render(request, 'En/News.html')


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
        return render(request, 'En/LoginSignup.html')


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
    return render(request, 'En/LoginSignup.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('forgot-mail')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uidb64 = user.id
            reset_link = request.build_absolute_uri(f'/ResetPassword/{uidb64}/{token}/')
            message = (f"""
                ______________________________
                Fa
                سلام{user.username}!
                
                
                ابن پیام صرافا برای بازگرداندن گذرواژه شما میباشد
                
                اگر بازگردادن پسورد خود اطمینان دارید, بر روی لینک زیر کلیک نمایید
                {reset_link}
                
                توجه داشته باشید این لینک معمولا یک بار مصرف است
                
                با تشکر تیم پشتیبانی TopUp
                ______________________________
                En
                Hi {user.username}!
                
                this message for reset password this {email} email
                if you want reset your password press link below!
                {reset_link}
                
                dont forget this link usually used for one time
                
                Thank you!
                The TopUP Team!
                this message CopyRighted by TopUP
                ______________________________""")

            send_mail(subject='Password Reset', message=message, from_email=EMAIL_HOST_USER, recipient_list=[email], fail_silently=False)
            return render(request, 'En/ForgotPassword_Done.html')
        except ObjectDoesNotExist:
            return HttpResponse("<h2>we have problem in send email<h2/>")
    return render(request, 'En/ForgotPassword.html')


def reset_password(request):
    # url = generated_url
    if request.method == 'GET':
        request.method(urlsafe_base64_encode())
    form = SetPasswordForm(user=request.user, data=request.POST.get('new_password1') or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Your password has been successfully reset.")
        return redirect('ResetPasswordDone')
    else:
        HttpResponse('<h2>we have problem in reset password, sorry dude!</h2>')
    return render(request, 'ResetPassword_Done.html')


def reset_password_done(request):
    render(request, 'En/ResetPassword_Done.html')


def forgot_password_done(request):
    render(request, 'En/ForgetPassword_Done.html')


def product(request):
    pass
