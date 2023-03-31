from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donation, name='donation'),
    path('donate/success/', views.donation_success, name='donation_success'),
    path('donate/cancel/', views.donation_cancel, name='donation_cancel'),
]
