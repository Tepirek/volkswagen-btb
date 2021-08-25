from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/summary/', summary_list),
    path('api/v1/summary/create/', generate_summary),
    path('api/v1/summary/<int:pk>/', summary_detail),
]