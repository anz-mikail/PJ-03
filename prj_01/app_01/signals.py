from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Response, Post


# @receiver(post_save, sender=Post)
# def post_created(instance, created, **kwargs):
#     if not created:
#         return
#
#     emails = User.objects.all().values_list('email', flat=True)
#
#     subject = f'Новое объявление {instance.title}'
#
#     text_content = (
#         f'Автор: {instance.author}\n'
#         f'Ссылка объявление: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Автор: {instance.author}<br>'
#         f'Категория: {instance.category}<br><br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на объявление</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()


# @receiver(pre_save, sender=Response)
# def handler(sender, instance, created, **kwargs):
#     if instance.status:
#         mail = instance.author.email
#         send_mail('ваш отклик принят', [mail], fail_silently=False,)
#     mail = instance.post.author.email
#     send_mail('ваш отклик не принят', [mail], fail_silently=False,)
