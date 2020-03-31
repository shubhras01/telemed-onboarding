from rest_framework import serializers
from . models import Doctor
import uuid, datetime
from . const import *

import freshdesk_api.constants as fd_const
from freshdesk_api.constants import AgentAPIFields
from freshdesk_api.public import create_agent


class DoctorSerializer(serializers.Serializer):
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

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Doctor.objects.get_or_create(**validated_data)
    # def create(self, validated_data):
    #     if not self.validated_data.get("id"):
    #         self.validated_data["id"] = uuid.uuid4().__str__()
    #     if not self.validated_data.get("onboarding_status"):
    #         self.validated_data["onboarding_status"] = ONBOARDING_QUEUE
    #     if not self.validated_data.get("created_at"):
    #         self.validated_data["created_at"] = datetime.datetime.now()
    #     if self.validated_data["onboarding_status"] == ONBOARDING_SUCCEED:
    #         freshdesk_status = self.create_freshdesk_agent()
    #         if freshdesk_status == 201:
    #             self.validated_data["freshdesk_agent_created"] = True
    #         # TODO: Log user id for which this fails
    #     created = Doctor.objects.get_or_create(mci=self.validated_data["mci"])
    #     return created
    #
    # def create_freshdesk_agent(self):
    #     req = {
    #         AgentAPIFields.email: self.data.get("email"),
    #         AgentAPIFields.name: self.data.get("name"),
    #         AgentAPIFields.mobile: str(self.data.get("contact_number")),
    #         AgentAPIFields.ticket_scope: fd_const.TICKET_SCOPE,
    #         AgentAPIFields.language: fd_const.LANGUAGE
    #     }
    #     return create_agent(req)
    #
    # def update(self, instance, validated_datah):
    #     # TODO add code here
    #     # instance.onboarding_status = validated_data.get('email', instance.email)
    #     # instance.content = validated_data.get('content', instance.content)
    #     # instance.created = validated_data.get('created', instance.created)
    #     return instance

    # def save(self):
    #     email = self.validated_data['email']
    #     message = self.validated_data['message']
    #     # send_email(from=email, message = message)

