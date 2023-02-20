from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addvehicles/', views.AddVehicle.as_view(), name='addvehicles'),
    path('updatevehicle/<int:pk>/',
         views.UpdateVehicle.as_view(), name='updatevehicle'),
    path('deletevehicle/<int:pk>/',
         views.DeleteVehicle.as_view(), name='deletevehicle'),
]
