
from django.contrib import admin
from django.urls import path
from config.views import index
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('', include('apps.m_user.urls')),
    path('tienda/', include('apps.m_tienda.urls')),
    path('carrito/', include('apps.m_carrito.urls')),
    path('administrador/', include('apps.m_admin.urls')),
    path('compra/', include('apps.m_compra.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)