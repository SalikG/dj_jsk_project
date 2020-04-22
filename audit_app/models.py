
from django.db import models
from login_app.models import UserProfile


class UserCreditAudit(models.Model):
    user_id = models.IntegerField()
    user_profile_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    credit_change = models.DecimalField(max_digits=6, decimal_places=2)
    credit_before = models.DecimalField(max_digits=6, decimal_places=2)
    credit_after = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} - {self.user_profile_id} - {self.first_name} - {self.last_name}' \
               f' - {self.credit_change} - {self.credit_before} - {self.credit_after} - {self.timestamp}'
