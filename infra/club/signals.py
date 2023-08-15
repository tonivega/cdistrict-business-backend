from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Player, Manager
import logging

logger = logging.getLogger("app")


@receiver(post_save, sender=Player)
@receiver(post_save, sender=Manager)
def create_profile(sender, instance, created, **kwargs):
    logger.info("Send email, slack message, whatever for {}".format(instance.friendly_name))


