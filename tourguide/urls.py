from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-suggestions/', views.get_suggestions, name='get_suggestions'),
]