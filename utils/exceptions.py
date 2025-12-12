from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

def custom_exception_handler(exc, context):
    """
    Manejador de excepciones personalizado para DRF.
    """
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
            response.data = {"error": "Sin Autenticación"}
            response.status_code = status.HTTP_401_UNAUTHORIZED

    return response
