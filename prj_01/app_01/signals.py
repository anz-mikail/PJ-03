from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Response


@receiver(pre_save, sender=Response)
def handler(sender, instance, created, **kwaegs):
    if instance.status:
        mail = instance.author.email
        send_mail(
            'pismo 1',
            [mail],
            fail_silently=False,
        )
    mail = instance.post.author.email
    send_mail(
        'pismo 2',
        [mail],
        fail_silently=False,
    )