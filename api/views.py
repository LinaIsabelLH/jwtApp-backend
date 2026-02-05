from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import permissions

# Create your views here.
class CustomTokenView(TokenObtainPairView):
    serializer_class= serializers.CustomTokenSerializer


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
