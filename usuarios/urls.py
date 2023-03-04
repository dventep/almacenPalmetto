from django.urls import path
from . import views

urlpatterns = [    
    path('', views.login),
    path('lista/', views.list_users),
    path('logout/', views.logout_function),
]