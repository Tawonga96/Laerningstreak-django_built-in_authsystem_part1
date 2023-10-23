from django.urls import path
from . import views 


urlpatterns=[
    path('register', views.UserAuthRegistration, name='register'),
    path('', views.UserAuthLogin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]