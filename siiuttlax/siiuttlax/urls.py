from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importaciones de las vistas personalizadas
from apps.justify.views import CustomLoginView, alumno_view, tutor_view, revisar_justificante_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.user_profile.urls')),
    path('', include('apps.academy.urls')),
    path('', include('apps.interview.urls')),
    path('', include('apps.testvak.urls')),
    path('', include('apps.group.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('reporte_tutoria/', include('apps.reporte_tutoria.urls', namespace='reporte_tutoria')),
    path('seguimiento/', include('apps.seguimiento.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('solicitar/', alumno_view, name='ruta_alumno'),
    path('revisar/', tutor_view, name='ruta_tutor'),
    path('revisar/justificante/<int:justificante_id>/', revisar_justificante_view, name='ruta_para_revisar_justificante'),
    path('vocational/', include('apps.vocational.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
