from django.urls import path, include
from .views import run_index, Login_Register

urlpatterns = [
    path('Home/', run_index),
    path('LoginSignup/', Login_Register)


]
