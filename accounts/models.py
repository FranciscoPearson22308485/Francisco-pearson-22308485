from django.db import models
from django.contrib.auth.models import User
import secrets
from datetime import timedelta
from django.utils import timezone

class MagicToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_valid(self):
        """Token válido por 15 minutos"""
        return timezone.now() < self.created_at + timedelta(minutes=15)
    
    @staticmethod
    def generate_token():
        """Gera token único"""
        return secrets.token_urlsafe(32)
    
    def __str__(self):
        return f"Token for {self.user.username}"