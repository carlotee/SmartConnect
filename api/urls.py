from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import api_info, UsuarioViewSet, DepartamentoViewSet
from gestion_dispositivos.views import SensorViewSet, BarreraViewSet
from control_acceso.views import EventoViewSet
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import LoginView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'sensores', SensorViewSet)
router.register(r'barreras', BarreraViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_obtain_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh_login'),

    path('info/', api_info, name='api_info'),
    path('', include(router.urls)),
]
