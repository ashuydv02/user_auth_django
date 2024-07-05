from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login_user'),
    path('register/', views.user_register, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.user_profile, name='profile'),
    path('change_password/', views.change_password, name='change_password')
]
