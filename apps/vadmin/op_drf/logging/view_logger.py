import logging

from django.db.models import Model
from rest_framework.request import Request
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class ViewLogger(object):
    def __init__(self, view=None, request=None, *args, **kwargs) -> None:
        super().__init__()
        self.view = view
        self.request = request
        self.model = None
        self.log_prefix: str = ''
        if self.view and hasattr(self.view.get_queryset(), 'models'):
            self.model: Model = self.view.get_queryset().model
        elif self.view and hasattr(self.view.get_serializer(), 'Meta') and hasattr(self.view.get_serializer().Meta,
                                                                                   'models'):
            self.model: Model = self.view.get_serializer().Meta.model
        if self.model:
            request.session['model_name'] = str(getattr(self.model, '_meta').verbose_name)

    def handle(self, request: Request, *args, **kwargs):
        pass

    def logger(self, msg):
        self.request.session['request_msg'] = msg
        return logger


class APIViewLogger(ViewLogger):
    def __init__(self, view=None, request=None, *args, **kwargs) -> None:
        super().__init__(view, request, *args, **kwargs)
        self.view: APIView = view
        self.request: Request = request
        self.user = request.user


class ModelViewLogger(APIViewLogger):
    def __init__(self, view=None, request=None, *args, **kwargs) -> None:
        super().__init__(view, request, *args, **kwargs)


class RelationshipViewLogger(APIViewLogger):
    def __init__(self, view=None, request=None, instanceId=None, *args, **kwargs) -> None:
        super().__init__(view, request)
        self.instanceId: str = instanceId

    def handle(self, request: Request, *args, **kwargs):
        """
        handle
        """

    pass


class CustomerRelationshipViewLogger(RelationshipViewLogger):
    def __init__(self, view=None, request=None, instanceId=None, *args, **kwargs) -> None:
        super().__init__(view, request, instanceId, *args, **kwargs)
        self.log_prefix: str = 'RelationshipView:'

    def handle_get(self, request: Request, *args, **kwargs):
        """
        GET
        """
        pass

    def handle_post(self, request: Request, *args, **kwargs):
        """
        POST
        """
        operator = self.user.username
        model_name = getattr(self.view.model, '_meta').verbose_name
        to_field_name = self.view.to_field_name
        to_model_name = getattr(self.view.relationship_model, '_meta').verbose_name
        self.logger(
            f'{self.log_prefix}用户[username={operator}]新增, {model_name}实例[{to_field_name}={self.instanceId}]与{to_model_name}的关联关系')

    def handle_put(self, request: Request, *args, **kwargs):
        """
        PUT
        """
        operator = self.user.username
        model_name = getattr(self.view.model, '_meta').verbose_name
        to_field_name = self.view.to_field_name
        to_model_name = getattr(self.view.relationship_model, '_meta').verbose_name
        self.logger(
            f'{self.log_prefix}username[username={operator}]operator, {model_name}model_name[{to_field_name}={self.instanceId}]与{to_model_name}model_name')

    def handle_delete(self, request: Request, *args, **kwargs):
        """
        DELETE
        """
        operator = self.user.username
        model_name = getattr(self.view.model, '_meta').verbose_name
        to_field_name = self.view.to_field_name
        to_model_name = getattr(self.view.relationship_model, '_meta').verbose_name
        self.logger(
            f'{self.log_prefix}username[username={operator}]operator, {model_name}model_name[{to_field_name}={self.instanceId}]与{to_model_name}model_name')


class CustomerModelViewLogger(ModelViewLogger):
    def __init__(self, view=None, request=None, *args, **kwargs) -> None:
        super().__init__(view, request, *args, **kwargs)
        self.log_prefix: str = 'CustomModelViewSetHistory:'

    def handle(self, request: Request, *args, **kwargs):
        pass

    def handle_retrieve(self, request: Request, instance: Model = None, *args, **kwargs):
        """
        retrieve(GET)
        """
        pass
        operator = self.user.username
        # model_name = getattr(self.model, '_meta').verbose_name
        # self.logger(f'{self.log_prefix}用户[username={operator}]检索{model_name}:[{instance}]')

    def handle_list(self, request: Request, *args, **kwargs):
        """
        list(GET)
        """
        pass
        operator = self.user.username
        # model_name = getattr(self.model, '_meta').verbose_name
        # self.logger(f'{self.log_prefix}用户[username={operator}]查询{model_name}')

    def handle_create(self, request: Request, instance: Model = None, *args, **kwargs):
        """
        create(POST)
        """
        pass
        operator = self.user.username
        # model_name = getattr(self.model, '_meta').verbose_name
        # self.logger(f'{self.log_prefix}用户[username={operator}]创建{model_name}:[{instance}]')

    def handle_update(self, request: Request, instance: Model = None, *args, **kwargs):
        """
        update(PUT)
        """
        pass
        operator = self.user.username
        # model_name = getattr(self.model, '_meta').verbose_name
        # self.logger(f'{self.log_prefix}用户[username={operator}]更新{model_name}:[{instance}]')

    def handle_partial_update(self, request: Request, instance: Model = None, *args, **kwargs):
        """
        partial_update(PATCH)
        """
        pass
        operator = self.user.username
        model_name = getattr(self.model, '_meta').verbose_name
        self.logger(f'{self.log_prefix}username[username={operator}]operator{model_name}:[{instance}]')

    def handle_destroy(self, request: Request, instance: Model = None, *args, **kwargs):
        """
        destroy(DELETE)
        """
        pass
        operator = self.user.username
        # model_name = getattr(self.model, '_meta').verbose_name
        # self.logger(f'{self.log_prefix}用户[username={operator}]删除{model_name}:[{instance}]')

    def handle_other(self, request: Request, instance: Model = None, *args, **kwargs):
        pass
        operator = self.user.username
        model_name = getattr(self.model, '_meta').verbose_name
        self.logger(f'{self.log_prefix}username[username={operator}]operator{model_name}:[{instance}]')
