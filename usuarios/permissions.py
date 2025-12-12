from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    message = "Sin Permisos"  # mensaje para errores 403

    def has_permission(self, request, view):

        # Si es GET/HEAD/OPTIONS → solo necesita estar autenticado
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Para POST / PUT / PATCH / DELETE → debe ser admin
        if not request.user.is_authenticated:
            return False

        return request.user.rol == 'admin'
