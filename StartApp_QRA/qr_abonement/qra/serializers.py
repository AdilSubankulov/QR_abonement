from rest_framework import serializers
from .models import Tariff, UserProfile, UserAbonement

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['unique_id', 'full_name', 'email']

class UserAbonementSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)
    tariff = TariffSerializer(read_only=True)

    class Meta:
        model = UserAbonement
        fields = ['unique_id', 'user_profile', 'tariff', 'days_count', 'is_active']