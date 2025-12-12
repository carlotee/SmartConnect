from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotAuthenticated

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raise NotAuthenticated("Sin Autenticación")

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise NotAuthenticated("Sin Autenticación")

        try:
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
        except Exception:
            raise NotAuthenticated("Sin Autenticación")
