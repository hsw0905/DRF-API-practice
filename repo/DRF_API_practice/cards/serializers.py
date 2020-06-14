from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.user_name')
    class Meta:
        model = Card
        fields = ['id', 'title', 'contents', 'owner', 'created_at', 'updated_at', 'is_reported']