from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('reservations/',include(('reservation.urls', 'reservation'),namespace = "reservartion")),
    path('delivery/', include('delivery.urls'), name = 'delivery'),
    path('api/',include('delivery.api.urls'), name = 'api'),
    path('home/', TemplateView.as_view(template_name='reservation/home.html'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
