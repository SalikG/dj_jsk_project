from secrets import token_urlsafe
from django.contrib.auth.models import User
from django.db import models
import datetime


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class UserProfile(models.Model):
    default_role_id = Role.objects.get(name="customer").id
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    birthday = models.DateField(default=datetime.date.min)
    # credit = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    experience = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=default_role_id)
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.role}'


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=43, default=token_urlsafe)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.created_timestamp}'
