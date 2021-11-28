from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='store-homepage'),
    path('about/', views.about, name='store-about'),
    path('contact/', views.contact, name='store-contact'),
    path('checkout/', views.checkout, name='store-checkout'),
]
