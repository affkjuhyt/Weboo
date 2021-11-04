from django.contrib.auth.models import User

from rest_framework import serializers

from payments.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
            "created_by",
            "plan_end_date"
        )
