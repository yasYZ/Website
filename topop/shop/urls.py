from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('Products/<int:pk_id>', views.products, name="Product"),
    path('Shop/', views.products, name="codes"),
]
