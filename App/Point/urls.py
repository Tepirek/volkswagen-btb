from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/points/summary/', summary_points),
    path('api/v1/points/', point_list),
    path('api/v1/points/<int:pk>/', point_detail),
]
