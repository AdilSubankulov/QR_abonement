from rest_framework import viewsets, permissions
from .models import Tariff, UserAbonement, UserProfile
from .serializers import TariffSerializer, UserAbonementSerializer, UserProfileSerializer

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff  # Разрешено только для администраторов

class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [IsAdminUser]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserAbonementViewSet(viewsets.ModelViewSet):
    queryset = UserAbonement.objects.all()
    serializer_class = UserAbonementSerializer
