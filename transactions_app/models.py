from django.db import models
from login_app.models import UserProfile


class CreditTransaction(models.Model):
    user = models.ForeignKey(UserProfile, related_name='credit_transaction', on_delete=models.CASCADE)
    credit_input = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.credit_input} - {self.timestamp}'
