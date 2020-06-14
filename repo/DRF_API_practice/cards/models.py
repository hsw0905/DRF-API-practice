from django.db import models

# Create your models here.
from account.models import Account


class Card(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    contents = models.TextField()
    owner = models.ForeignKey(Account, related_name='cards', on_delete=models.CASCADE, )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_reported = models.BooleanField(default=False)

    class Meta:
        ordering = ['updated_at']