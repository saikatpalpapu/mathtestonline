from django.urls import path
from mathtestapi import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('login/<int:pk>/', views.login),
]