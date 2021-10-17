import django_filters
from rest_framework import filters


class DatetimeRangeFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_filed = view.range_filed_name
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')

        if from_date is not None and to_date is not None:
            lookup = '%s__range' % filter_filed
            return queryset.filter(**{lookup: (from_date, to_date)})
        else:
            if from_date is not None:
                queryset.filter(**{'%s__gte' % filter_filed: from_date})
            if to_date is not None:
                queryset.filter(**{'%s__lte' % filter_filed: to_date})
        return queryset


class DateTimeFilter(django_filters.FilterSet):
    from_date = django_filters.DateTimeFilter(field_name='date_added', lookup_expr='gte')
    to_date = django_filters.DateTimeFilter(field_name='date_added', lookup_expr='lte')

    class Meta:
        fields = ['from_date', 'to_date']
        abstract = True
