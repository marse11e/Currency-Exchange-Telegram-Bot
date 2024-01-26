from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TelegramAds
from .bot import ads


@receiver(post_save, sender=TelegramAds)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ads(instance)