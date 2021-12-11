from django_celery_beat.admin import TaskSelectWidget
from django_celery_beat.models import IntervalSchedule, CrontabSchedule, PeriodicTask
from rest_framework.views import APIView

from apps.vadmin.celerys.filters import IntervalScheduleFilter, CrontabScheduleFilter, PeriodicTaskFilter
from apps.vadmin.celerys.serializers import IntervalScheduleSerializer, CrontabScheduleSerializer, \
    PeriodicTaskSerializer
from apps.vadmin.op_drf.views import CustomAPIView
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.op_drf.response import SuccessResponse


class IntervalScheduleModelViewSet(CustomModelViewSet):
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer
    create_serializer_class = IntervalScheduleSerializer
    update_serializer_class = IntervalScheduleSerializer
    filter_class = IntervalScheduleFilter
    search_fields = ('every', 'period')
    ordering = 'every'


class CrontabScheduleModelViewSet(CustomModelViewSet):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer
    filter_class = CrontabScheduleFilter
    search_fields = ('minute', 'hour')
    ordering = 'minute'


class PeriodicTaskModelViewSet(CustomModelViewSet):
    queryset = PeriodicTask.objects.exclude(name="celery.backend_cleanup")
    serializer_class = PeriodicTaskSerializer
    filter_class = PeriodicTaskFilter
    search_fields = ('name', 'task', 'date_changed')
    ordering = 'date_changed'


class TasksAsChoices(APIView):
    def get(self, request):
        lis = []

        def get_data(datas):
            for item in datas:
                if isinstance(item, (str, int)) and item:
                    lis.append(item)
                else:
                    get_data(item)

        get_data(TaskSelectWidget().tasks_as_choices())
        return SuccessResponse(list(set(lis)))


class OperateCeleryTask(CustomAPIView):
    def post(self, request):
        req_data = request.data
        task = req_data.get('celery_name', '')
        data = {
            'task': ''
        }
        test = f"""
from {'.'.join(task.split('.')[:-1])} import {task.split('.')[-1]}
task = {task.split('.')[-1]}.delay()
        """
        exec(test, data)
        return SuccessResponse({'task_id': data.get('task').id})
