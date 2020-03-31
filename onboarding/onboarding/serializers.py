from rest_framework_mongoengine import serializers
from . models import Doctor


class DoctorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Doctor
        fields = ("id",
                  "name",
                  "email",
                  "medical_qual",
                  "mci",
                  "state_authority",
                  "contact_number",
                  "other_contact",
                  "time_pref",
                  "language",
                  "organisation_name",
                  "doctor_type",
                  "duty_hours",
                  "onboarding_status",
                  "freshdesk_agent_created",
                  "comment")
        depth = 2
