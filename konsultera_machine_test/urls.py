from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicle_details.urls')),
    path('accounts/', include('accounts.urls')),
]
