from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/users/', user_list),
    path('api/v1/users/<int:pk>/', user_detail),
    path('auth/user/', user_auth)
]