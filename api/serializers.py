from rest_framework import serializers
from .models import Info

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields='__all__'