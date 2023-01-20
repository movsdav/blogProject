from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blogApp.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
