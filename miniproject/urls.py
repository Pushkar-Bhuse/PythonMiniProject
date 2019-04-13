from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from reservation import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/',include('reservation.urls'),name = 'reservation'),
    path('delivery/', include('delivery.urls'), name = 'delivery'),
    path('api/',include('delivery.api.urls'), name = 'api'),
    path('', views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
