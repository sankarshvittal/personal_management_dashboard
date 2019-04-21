from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal_management_dashboard_home/', include('personal_management_dashboard_home.urls')),
]
