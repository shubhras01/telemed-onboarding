from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
import uuid, datetime

from rest_framework import serializers, viewsets, response

from . const import MEDICAL_QUAL_CHOICES, TIME_PREF_CHOICES, LANGUAGE_CHOICE, \
    DEDICATE_HOURS_CHOICE, ONBOARDING_FAIL, ONBOARDING_QUEUE, ONBOARDING_REJECTED,\
    ONBOARDING_SUCCEED, ONBOARDING_UNQUALIFIED, TMV, TMP

import freshdesk_api.constants as fd_const
from freshdesk_api.constants import AgentAPIFields
from freshdesk_api.public import create_agent

DOCTORS_TYPS = [TMP, TMV]


class Doctor(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=100)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    medical_qual = models.CharField(choices=tuple(zip(MEDICAL_QUAL_CHOICES, MEDICAL_QUAL_CHOICES)), max_length=10)
    mci = models.IntegerField(null=False, unique=True)
    state_authority = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10, null=False)
    other_contact = models.CharField(max_length=10, null=True)
    time_pref = models.CharField(choices=tuple(zip(TIME_PREF_CHOICES, TIME_PREF_CHOICES)), max_length=10)
    language = ArrayField(models.CharField(max_length=10, blank=False))
    organisation_name = models.CharField(max_length=100)
    doctor_type = models.CharField(choices=tuple(zip(DOCTORS_TYPS, DOCTORS_TYPS)), max_length=10)
    duty_hours = models.CharField(choices=tuple(zip(DEDICATE_HOURS_CHOICE, DEDICATE_HOURS_CHOICE)), max_length=10)
    onboarding_status = models.CharField(choices=((ONBOARDING_SUCCEED, ONBOARDING_SUCCEED),
                                        (ONBOARDING_FAIL, ONBOARDING_FAIL),
                                        (ONBOARDING_REJECTED, ONBOARDING_REJECTED),
                                        (ONBOARDING_UNQUALIFIED, ONBOARDING_UNQUALIFIED),
                                        (ONBOARDING_QUEUE, ONBOARDING_QUEUE)), max_length=20)
    created_at = models.DateTimeField(auto_now_add=datetime.datetime.now())
    freshdesk_agent_created = models.BooleanField(default=False)
    comment = models.CharField(max_length=200)
    meta_status = models.CharField(max_length=100)

    def create(self, *args, **kwargs):
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
        return super(Doctor, self).create(*args, **kwargs)

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
        return create_agent(req)


 class Language(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=100)
    language = models.CharField(max_length=10, blank=False)
    group_id = models.IntegerField()

