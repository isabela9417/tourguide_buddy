from django.urls import path
from . import views
from .views import province_tourism_sites

urlpatterns = [
    path('', views.home, name='home'),
    path('get-suggestions/', views.get_suggestions, name='get_suggestions'),
    path('tourism-sites/<slug:province_name>/', views.province_tourism_sites, name='province_tourism_sites'),
]