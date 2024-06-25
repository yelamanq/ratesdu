from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('teacher/', include('teacher.urls')),
    path('user/', include('user.urls')),
    path('cabinet/', include('cabinet.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
