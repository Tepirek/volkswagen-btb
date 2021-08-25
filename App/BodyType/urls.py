from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/body-types/', body_type_list),
    path('api/v1/body-types/<int:pk>/', body_type_detail),
]