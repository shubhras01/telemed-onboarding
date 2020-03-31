from mongoengine import EmbeddedDocument, fields, Document
from django.contrib.postgres.fields import JSONField
import uuid, datetime

from rest_framework import serializers, viewsets, response

from . const import MEDICAL_QUAL_CHOICES, TIME_PREF_CHOICES, LANGUAGE_CHOICE, DEDICATE_HOURS_CHOICE, ONBOARDING_FAIL, ONBOARDING_QUEUE, ONBOARDING_REJECTED, ONBOARDING_SUCCEED, ONBOARDING_UNQUALIFIED, TMV, TMP
import freshdesk_api.constants as fd_const
from freshdesk_api.constants import AgentAPIFields
from freshdesk_api.public import create_agent

DOCTORS_TYPS = [TMP, TMV]


class Doctor(Document):
    id = fields.StringField(primary_key=True)
    name = fields.StringField(max_length=100, null=False)
    email = fields.EmailField(max_length=100, null=False)
    medical_qual = fields.StringField(choices=tuple(zip(MEDICAL_QUAL_CHOICES, MEDICAL_QUAL_CHOICES)))
    mci = fields.IntField(null=False)
    state_authority = fields.StringField(max_length=100)
    contact_number = fields.StringField(max_length=10, null=False)
    other_contact = fields.StringField(max_length=10, null=True)
    time_pref = fields.StringField(choices=tuple(zip(TIME_PREF_CHOICES, TIME_PREF_CHOICES)))
    language = fields.ListField(null=False)
    organisation_name = fields.StringField(max_length=100)
    doctor_type = fields.StringField(choices=tuple(zip(DOCTORS_TYPS, DOCTORS_TYPS)))
    duty_hours = fields.StringField(choices=tuple(zip(DEDICATE_HOURS_CHOICE, DEDICATE_HOURS_CHOICE)))
    onboarding_status = fields.StringField(choices=((ONBOARDING_SUCCEED, ONBOARDING_SUCCEED),
                                        (ONBOARDING_FAIL, ONBOARDING_FAIL),
                                        (ONBOARDING_REJECTED, ONBOARDING_REJECTED),
                                        (ONBOARDING_UNQUALIFIED, ONBOARDING_UNQUALIFIED),
                                        (ONBOARDING_QUEUE, ONBOARDING_QUEUE)))
    created_at = fields.DateTimeField(auto_now_add=datetime.datetime.now())
    freshdesk_agent_created = fields.BooleanField(default=False)
    comment = fields.StringField()
    meta_status = fields.StringField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4().__str__()
        if not self.onboarding_status:
            self.onboarding_status = ONBOARDING_QUEUE
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        if self.onboarding_status == ONBOARDING_SUCCEED:
            freshdesk_status = self.create_freshdesk_agent()
            if freshdesk_status == 201:
                self.freshdesk_agent_created = True
            # TODO: Log user id for which this fails
        return super(Doctor, self).save(*args, **kwargs)


    def create_freshdesk_agent(self):
        req = {
            AgentAPIFields.email: self.email,
            AgentAPIFields.name: self.name,
            AgentAPIFields.mobile: str(self.contact_number),
            AgentAPIFields.ticket_scope: fd_const.TICKET_SCOPE,
            AgentAPIFields.language: fd_const.LANGUAGE
        }
        return create_agent(reg)
 