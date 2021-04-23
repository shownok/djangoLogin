from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name='registerPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('', views.indexPage, name='indexPage'),
    path('dashboard/', views.DashBoard, name='dashboard'),
]
