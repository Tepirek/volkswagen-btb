from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/error-types/', error_type_list),
    path('api/v1/error-types/<int:pk>/', error_type_detail),
]