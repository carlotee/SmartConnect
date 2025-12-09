from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import api_info, UsuarioViewSet, DepartamentoViewSet
from gestion_dispositivos.views import SensorViewSet, BarreraViewSet
from control_acceso.views import EventoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'sensores', SensorViewSet)
router.register(r'barreras', BarreraViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info/', api_info, name='api_info'),
    path('', include(router.urls)),
]