
from rest_framework import serializers
from .models import Account

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'  # You can customize this list based on your needs
