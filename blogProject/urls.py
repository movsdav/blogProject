from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blogApp.urls')),
    path('accounts/', include('authApp.urls')),
    path('admin/', admin.site.urls),
    path('auth-api/', include('rest_framework.urls')),
    path('api/v1/', include('api.v1.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
