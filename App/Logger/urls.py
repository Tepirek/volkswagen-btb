from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/logs/', log_list),
    path('api/v1/logs/<int:pk>/', log_detail),
]
