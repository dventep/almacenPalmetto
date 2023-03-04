from django.urls import path
from . import views
print('agua')
urlpatterns = [    
    path('', views.home),
    path('getProduct/', views.getProduct),
    path('deleteProduct/', views.deleteProduct),
]