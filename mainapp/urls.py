from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login',views.handleLogin),
    path('signup',views.handleSignup),
    path('password',views.password),
    path('mypasswords',views.showPassword),
    path('error',views.error),
]
