from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'), name='main'),
    path('users/', include('django.contrib.auth.urls')),
    path('login/', include('to_do.urls')),
]