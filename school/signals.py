from django.db.models.signals import pre_save
from django.dispatch import receiver

from school.models import Students


@receiver(pre_save, sender=Students)
def my_callback(sender, **kwargs):
    print(f"Model saved! Sender was: {sender} kwargs were: {kwargs}")
