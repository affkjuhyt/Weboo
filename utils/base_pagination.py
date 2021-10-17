from django.db.models import Avg, Max, Min, Sum

from rest_framework.pagination import PageNumberPagination


class BasePageNumberPagination(PageNumberPagination):
    """
    A json-apis compatible pagination format
    """

    page_size_query_param = 'page_size'
    max_page_size = 500

    def paginate_queryset(self, queryset, request, view=None):
        self.extra_data = {}
        try:
            legit_fields = view.aggregate_fields
            aggregate_fields = request.query_params.getlist('extra_fields')
            set(aggregate_fields).intersection_update(set(legit_fields))  # Remove fields that not allow
            if aggregate_fields:
                for field in aggregate_fields:
                    self.extra_data.update(queryset.aggregate(Avg(field), Sum(field), Max(field), Min(field)))
        except AttributeError:
            pass
        return super(BasePageNumberPagination, self).paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        paginated_response = super(BasePageNumberPagination, self).get_paginated_response(data)
        paginated_response.data['extra_data'] = self.extra_data
        return paginated_response
