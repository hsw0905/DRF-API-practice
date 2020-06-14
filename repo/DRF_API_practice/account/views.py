from rest_framework import viewsets
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import AllowAny

from account.models import Account
from account.serializers import UserSerializer
from cards.permissions import IsCardsOwner


class CustomPagination(CursorPagination):
    ordering = '-id'

class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['update','destroy']:
            return [IsCardsOwner()]
        elif self.action == ['list','retrieve']:
            return [AllowAny()]

        return super().get_permissions()

    def perform_destroy(self, instance):
        # 토큰 삭제해야 하는 부분
        instance.delete()
