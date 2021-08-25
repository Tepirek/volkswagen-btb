from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/actions/', action_list),
    path('api/v1/actions/<int:pk>/', action_detail),
]
