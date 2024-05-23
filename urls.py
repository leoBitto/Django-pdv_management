from django.urls import path
from . import views

app_name = 'pdv_management'

urlpatterns = [
    path('', views.pdv_dashboard, name='pdv_dashboard'),
    path('<uuid:pdv_id>/', views.pdv_update_delete, name='pdv_update_delete'),
    path('add_pdv/', views.pdv_dashboard, name='pdv_add'),
    
    path('opening-hours/', views.opening_hours_dashboard, name='opening_hours_dashboard'),
    path('opening-hours/<int:pk>/', views.opening_hours_update_delete, name='opening_hours_update_delete'),
    path('opening-hours/add/', views.opening_hours_create, name='opening_hours_add'),
]
