from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions_app.models import CreditTransaction
from login_app.models import UserProfile
from audit_app.models import UserCreditAudit


@receiver(post_save, sender=CreditTransaction, dispatch_uid="create_user_credit_audit")
def create_user_credit_audit(sender, instance, **kwargs):
    print("**** signal received")
    print(sender)
    print(kwargs)
    user_profile = instance.user
    user_credit_audit = UserCreditAudit()
    user_credit_audit.user_id = user_profile.user.pk
    user_credit_audit.user_profile_id = user_profile.pk
    user_credit_audit.first_name = user_profile.user.first_name
    user_credit_audit.last_name = user_profile.user.last_name
    user_credit_audit.credit_change = instance.credit_input
    user_credit_audit.credit_before = instance.credit_before
    user_credit_audit.credit_after = user_profile.credit
    user_credit_audit.save()



