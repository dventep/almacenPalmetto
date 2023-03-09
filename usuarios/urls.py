from django.urls import path
from . import views

urlpatterns = [    
    path('', views.login),
    path('lista/', views.list_users),
    path('logout/', views.logout_function),
    path('getUser/', views.getUser),
    path('goToUser/', views.goToUser),
    path('createUser/', views.createUser),
    path('putUser/', views.putUser),
    path('deleteUser/', views.deleteUser),
]