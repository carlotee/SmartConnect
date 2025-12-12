from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied

def custom_exception_handler(exc, context):

    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        return Response(
            {"Error": "Sin Autenticación"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if isinstance(exc, PermissionDenied):
        return Response(
            {"Error": "Sin Permisos"},
            status=status.HTTP_403_FORBIDDEN
        )

    response = exception_handler(exc, context)
    return response
