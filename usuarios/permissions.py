from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated as DRFIsAuthenticated

class CustomIsAuthenticated(DRFIsAuthenticated):
    message = 'Sin Autenticación'

class IsAdminOrReadOnly(permissions.BasePermission):
    
    message = 'Sin Permisos'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user and request.user.is_authenticated and request.user.rol == 'admin'