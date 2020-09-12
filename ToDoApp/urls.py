from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'user/', include('accounts.urls')),
    path(r'todo/', include('todos.urls')),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
