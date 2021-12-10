from rest_framework.validators import UniqueValidator, qs_exists

from apps.vadmin.util.exceptions import APIException


class CustomUniqueValidator(UniqueValidator):
    def __call__(self, value, serializer_field):
        field_name = serializer_field.source_attrs[-1]
        instance = getattr(serializer_field.parent, 'instance', None)

        queryset = self.queryset
        queryset = self.filter_queryset(value, queryset, field_name)
        queryset = self.exclude_current_instance(queryset, instance)
        if qs_exists(queryset):
            raise APIException(message=self.message)

    def __repr__(self):
        return super().__repr__()
