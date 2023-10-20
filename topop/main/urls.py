from django.urls import path, include
from .views import run_index, Login_Register, run_codes_page, news, contactus, register, forgot_password, product, log_out

urlpatterns = [
    path('Home/', run_index, name="Home"),
    path('LoginSignup/', Login_Register, name="LoginSignup"),
    path('Shop/', run_codes_page, name="codes"),
    path('News/', news, name="news"),
    path('ContactUs/', contactus, name="Contactus"),
    path('Register/', register, name="Register"),
    path('Logout/', log_out, name="Logout"),
    path('ForgotPassword/', forgot_password, name="forgot_password"),
    path('Product/', product, name="Product"),
]
