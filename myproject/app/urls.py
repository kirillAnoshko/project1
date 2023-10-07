from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('new_year/', views.greet)
]
