from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Action
    path('', include('Action.urls')),

    # BodyType
    path('', include('BodyType.urls')),
    
    # Color
    path('', include('Color.urls')),
    
    # ComponentType
    path('', include('ComponentType.urls')),
    
    # ErrorType
    path('', include('ErrorType.urls')),
    
    # InclusionType
    path('', include('InclusionType.urls')),
    
    # Logger
    path('', include('Logger.urls')),
    
    # Point
    path('', include('Point.urls')),
    
    # Report
    path('', include('Report.urls')),
    
    # User
    path('', include('User.urls')),

    # Summary
    path('', include('Summary.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# TODO: remove  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) from production !!!