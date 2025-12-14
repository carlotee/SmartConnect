from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise NotAuthenticated("Sin Autenticación")

        try:
            validated_token = self.get_validated_token(raw_token)
            user = self.get_user(validated_token)
            return (user, validated_token)

        except (InvalidToken, TokenError):
            raise NotAuthenticated("Sin Autenticación")
