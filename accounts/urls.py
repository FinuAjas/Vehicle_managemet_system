from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.Signin.as_view(), name='login'),
    path('logout/', views.Signout.as_view(), name='logout'),
]
