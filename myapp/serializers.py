from rest_framework import serializers
from .models import TGUserModel


class TGUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TGUserModel
        fields = '__all__'
