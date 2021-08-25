from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/component-types/', component_type_list),
    path('api/v1/component-types/<int:pk>/', component_type_detail),
]