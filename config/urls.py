from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/book/', include('book.urls')),
    path('api/v1/file/', include('file.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
