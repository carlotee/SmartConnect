from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 401:
            view = context.get('view', None)
            if view and getattr(view, 'permission_classes', None):
                if any(cls.__name__ == 'AllowAny' for cls in view.permission_classes):
            response.data = {"error": "Acceso denegado"}
    
    return response
