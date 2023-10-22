from django.urls import path
from django.views.generic import RedirectView
from .views import run_index, Login_Register, run_codes_page, news, contactus, register, forgot_password, product, log_out, reset_password, reset_password_done, forgot_password_done

urlpatterns = [
    path('', RedirectView.as_view(url="/Home", permanent=True)),
    path('Home/', run_index, name="Home"),
    path('LoginSignup/', Login_Register, name="LoginSignup"),
    path('Shop/', run_codes_page, name="codes"),
    path('News/', news, name="news"),
    path('ContactUs/', contactus, name="Contactus"),
    path('Register/', register, name="Register"),
    path('Logout/', log_out, name="Logout"),
    path('ForgotPassword/', forgot_password, name="forgot_password"),
    path('ResetPassword/<uid64>/<token>/', reset_password, name="password_reset"),
    path('ResetPasswordDone/', reset_password_done, name="reset_password_done_pg"),
    path('ForgetPasswordDone/', forgot_password_done, name="forget_password_done_pg"),
    path('Product/', product, name="Product"),
]
