from django.urls import path

from . import views 

urlpatterns = [
    path('_login', views._login, name='_login'), 
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'), 
] 