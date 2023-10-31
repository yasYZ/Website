from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from topop.settings import EMAIL_HOST_USER


def run_index(request):
    return render(request, 'En/index.html')


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
            uidb64 = user.id
            token = default_token_generator.make_token(user)
            reset_link = request.build_absolute_uri(f'/ResetPassword/{uidb64}/{token}/')
            message = f"""
                ______________________________
                Fa
                سلام {user.username}!


                این پیام برای بازیابی گذرواژه شما می‌باشد.

                اگر می‌خواهید گذرواژه خود را بازیابی کنید، لطفاً روی لینک زیر کلیک کنید:
                {reset_link}

                توجه داشته باشید که این لینک معمولاً یک بار مصرف است.

                با تشکر،
                تیم پشتیبانی TopUp
                ______________________________
                En
                Hi {user.username}!

                This message is for resetting your password.

                If you want to reset your password, please click on the link below:
                {reset_link}

                Please note that this link is usually for one-time use.

                Thank you,
                The TopUP Team!
                This message is CopyRighted by TopUP
                ______________________________"""

            send_mail(subject='Password Reset', message=message, from_email=EMAIL_HOST_USER,
                      recipient_list=[email], fail_silently=False)
            return render(request, 'En/ForgotPassword_Done.html')
        except ObjectDoesNotExist:
            return HttpResponse("<h2>We encountered a problem while sending the email.</h2>")
    return render(request, 'En/ForgotPassword.html')


def reset_password(request, uidb64, token):
    uid = int(uidb64)
    user = User.objects.get(pk=uid)
    context = {
        'uidb64': uidb64,
        'token': token
    }
    if request.method == 'POST':
        new_password = request.POST.get('new_password1')
        conf_password = request.POST.get('new_password2')
        if new_password == conf_password:
            user.set_password(new_password)
            user.save()
            messages.success(request, "Your password is successfully changed")
            return redirect('Home')
        else:
            messages.error(request, "Your password doesnt match")
    return render(request, 'En/ResetPassword.html', context)


def reset_password_done(request):
    render(request, 'En/ResetPassword_Done.html')


def forgot_password_done(request):
    render(request, 'En/ForgetPassword_Done.html')


def custom_404(request, exception):
    return render(request, 'En/ResetPassword_Done.html', status=404)
