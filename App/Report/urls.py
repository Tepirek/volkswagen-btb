from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/reports/', report_list),
    path('api/v1/reports/blueprint/<int:pk>/', blueprint),
    path('api/v1/reports/<int:pk>/', report_detail),
]