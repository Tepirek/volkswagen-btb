from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/inclusion-types/', inclusion_type_list),
    path('api/v1/inclusion-types/<int:pk>/', inclusion_type_detail),
]
