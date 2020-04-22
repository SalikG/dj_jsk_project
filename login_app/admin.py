from django.contrib import admin
from .models import PasswordResetRequest, UserProfile, Role
# Register your models here.
admin.site.register(PasswordResetRequest)
admin.site.register(UserProfile)
admin.site.register(Role)
