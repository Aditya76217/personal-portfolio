from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.submit_contact, name='api_contact'),
]
