from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from apps.vadmin.celerys.views import IntervalScheduleModelViewSet, CrontabScheduleModelViewSet, \
    PeriodicTaskModelViewSet, TasksAsChoices, \
    OperateCeleryTask

router = DefaultRouter()
router.register(r'intervalschedule', IntervalScheduleModelViewSet)
router.register(r'crontabschedule', CrontabScheduleModelViewSet)
router.register(r'periodictask', PeriodicTaskModelViewSet)

urlpatterns = format_suffix_patterns([
    url(r'^tasks_as_choices/', TasksAsChoices.as_view()),
    url(r'^operate_celery/', OperateCeleryTask.as_view()),
])

urlpatterns += router.urls
