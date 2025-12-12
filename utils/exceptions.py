from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

def custom_exception_handler(exc, context):
    # Interceptamos errores de autenticación
    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        return Response({"error": "Sin Autenticación"}, status=status.HTTP_401_UNAUTHORIZED)

    # Para otros errores, usamos el manejador por defecto
    response = exception_handler(exc, context)
    return response
