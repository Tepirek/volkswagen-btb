from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/colors/', color_list),
    path('api/v1/colors/<int:pk>/', color_detail),
]