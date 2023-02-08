from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api_v1/', include('app.urls'), name='api_v1'),
    path('admin/', admin.site.urls),
]
