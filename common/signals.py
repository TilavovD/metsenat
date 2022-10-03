from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StudentSponsor


@receiver(post_save, sender=StudentSponsor)
def my_handler(sender, instance, created, **kwargs):
    if created:
        sponsor = instance.sponsor
        sponsor.total_amount -= instance.amount
        sponsor.spent_amount += instance.amount
        sponsor.save()

        student = instance.student
        student.received_amount += instance.amount
        student.save()
