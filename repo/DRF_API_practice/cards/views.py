
# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import AllowAny

from cards.models import Card
from cards.permissions import IsCardsOwner
from cards.serializers import CardSerializer


class CustomPagination(CursorPagination):
    ordering = '-id'

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_permissions(self):
        if self.action in ['create','update','destroy']:
            return [IsCardsOwner()]
        elif self.action == ['list','retrieve']:
            return [AllowAny()]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)