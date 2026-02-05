from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import permissions


class CustomTokenView(TokenObtainPairView):
    """
    Cette vue gère la connexion :
    - Crée un pair de tokens (access + refresh) via le serializer personnalisé
    - Stocke le refresh token dans un cookie HttpOnly (inaccessible depuis JS)
    - Supprime le refresh token du corps de la réponse pour sécurité
    """
    serializer_class = serializers.CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        refresh_token = response.data["refresh"]

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=False,
            samesite="Lax",
        )

        del response.data["refresh"]

        return response


class CookieRefreshView(APIView):
    """
    Cette vue permet de renouveler l'access token automatiquement :
    - Le refresh token est lu depuis le cookie HttpOnly
    - Si le refresh token est présent et valide, un nouvel access token est renvoyé
    - Si absent ou invalide, renvoie une erreur 401
    """
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({"detail": "No refresh token"}, status=401)

        token = RefreshToken(refresh_token)
        return Response({"access": str(token.access_token)})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me_view(request):
    return Response({"message":"Ceci sont vos informations de profil."})


@api_view(["GET"])
@permission_classes([permissions.IsAdminUserCustom])
def admin_panel(request):
    return Response({"message":"Bienvenu(e) dans le panneau d'administration."})


@api_view(["GET"])
@permission_classes([permissions.IsPremiumUser])
def premium_data(request):
    return Response({"message":"Voici les données réservées aux membres Premium et Unlimited."})
