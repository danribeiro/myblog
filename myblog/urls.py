from django.contrib import admin
from django.urls import path, include
from core.views import home, single
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('home/', home, name = "home"),
    path('articles/<slug:str>', single, name = "single"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)