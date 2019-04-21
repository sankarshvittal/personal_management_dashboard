from django.urls import path
from .import views

app_name = 'personal_management_dashboard_home'

urlpatterns = [
    path('', views.personal_management_dashboard_home, name='personal_management_dashboard_home'),
    path('holiday_details/', views.holiday_details, name='holiday_details'),
    path('about_page/', views.about_page, name='about_page'),
]