from django.urls import path, include
from .views import run_index, Login_Register, run_codes_page, news, contactus

urlpatterns = [
    path('Home/', run_index, name="Home"),
    path('LoginSignup/', Login_Register, name="LoginSignup"),
    path('Shop/', run_codes_page, name="codes"),
    path('News/', news, name="news"),
    path('Contactus/', contactus, name="Contactus"),
]
