from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-1/', include('posts.urls')),
    path('api-2/', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
