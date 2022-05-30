
from django.urls import path
from .views import cross

urlpatterns = [
    path('', cross),
]