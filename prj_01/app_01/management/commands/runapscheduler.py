# import logging
# import datetime
#
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.triggers.cron import CronTrigger
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.core.management.base import BaseCommand
# from django.template.loader import render_to_string
# from django_apscheduler import util
# from django_apscheduler.jobstores import DjangoJobStore
# from django_apscheduler.models import DjangoJobExecution
# from django.utils import timezone
#
# from app_01.models import Post
#
# logger = logging.getLogger(__name__)
#
#
# def my_job():
#     today = timezone.now()
#     last_week = today - datetime.timedelta(days=7)
#     posts = Post.objects.filter(dateCreation__gte=last_week)
#     categories = set(posts.values_list('postCategory__name', flat=True))
#     subscribers = set(Post.objects.filter(name__in=categories).values_list('subscriptions__user__email', flat=True))
#     html_content = render_to_string('daily_post.html',
#                                     {'link': f'http://127.0.0.1:8000/post',
#                                      'posts': posts,
#                                      })
#     msg = EmailMultiAlternatives(
#         subject='новости недели',
#         body='',
#         from_email="test.skillfactory@yandex.ru",
#         to=subscribers,
#     )
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
#
# @util.close_old_connections
# def delete_old_job_executions(max_age=604_800):
#     DjangoJobExecution.objects.delete_old_job_executions(max_age)
#
#
# class Command(BaseCommand):
#     help = "Runs APScheduler."
#
#     def handle(self, *args, **options):
#         scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
#         scheduler.add_jobstore(DjangoJobStore(), "default")
#
#         scheduler.add_job(
#             my_job,
#              trigger=CronTrigger(second="*/5"),
#            # trigger=CronTrigger(day_of_week='fri', hour="18", minute="00"),
#             id="my_job",
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info("Added job 'my_job'.")
#
#         scheduler.add_job(
#             delete_old_job_executions,
#             trigger=CronTrigger(
#                 day_of_week="mon", hour="00", minute="00"
#             ),
#             id="delete_old_job_executions",
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info("Added weekly job: 'delete_old_job_executions'.")
#
#         try:
#             logger.info("Starting scheduler...")
#             scheduler.start()
#         except KeyboardInterrupt:
#             logger.info("Stopping scheduler...")
#             scheduler.shutdown()
#             logger.info("Scheduler shut down successfully!")
