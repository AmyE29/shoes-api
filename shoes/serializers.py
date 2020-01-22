from rest_framework import serializers
from .models import Shoes

class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = ['id', 'author', 'brand', 'style', 'created_at']
    