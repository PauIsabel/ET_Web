from django.urls import path
from . import views


urlpatterns = [
    path('api_clima/', views.api_clima, name='api_clima'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
]