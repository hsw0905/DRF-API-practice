from rest_framework import serializers
from .models import Account
from cards.serializers import CardSerializer


class UserSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'cards', 'date_joined',]