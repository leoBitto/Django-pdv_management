from django.urls import path
from . import views

app_name = 'pdv_management'

urlpatterns = [
    path('', views.pdv_dashboard, name='pdv_dashboard'),
    path('delete/<uuid:pdv_id>/', views.pdv_delete, name='pdv_delete'),
    path('update/<uuid:pdv_id>/', views.pdv_update, name='pdv_update'),
    path('add_pdv/', views.pdv_add, name='pdv_add'),
    
    path('opening-hours/', views.opening_hours_dashboard, name='opening_hours_dashboard'),
    path('opening-hours/delete/<int:opening_hours_id>/', views.opening_hours_delete, name='opening_hours_delete'),
    path('opening-hours/update/<int:opening_hours_id>/', views.opening_hours_update, name='opening_hours_update'),
    path('opening-hours/add/', views.opening_hours_add, name='opening_hours_add'),
]
