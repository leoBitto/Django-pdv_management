from django.urls import path
from .views import *

app_name = 'pdv_management'

urlpatterns = [
    path('dashboard/', PDVDashboardView.as_view(), name='pdv_dashboard'),
    

]
