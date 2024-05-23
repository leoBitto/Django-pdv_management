from django.urls import path
from . import views

app_name = 'pdv_management'

urlpatterns = [
    path('', views.pdv_manage, name='pdv_manage'),
    path('delete/<int:pk>/', views.pdv_delete, name='pdv_delete'),
    path('create/', views.pdv_create, name='pdv_create'),
    path('update/<int:pk>/', views.pdv_update, name='pdv_update'),
]
