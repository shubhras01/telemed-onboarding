from mongoengine import EmbeddedDocument, fields, Document
from django.contrib.postgres.fields import JSONField
import uuid

from rest_framework import serializers, viewsets, response

from . const import MEDICAL_QUAL_CHOICES, TIME_PREF_CHOICES, LANGUAGE_CHOICE, DEDICATE_HOURS_CHOICE, ONBOARDING_FAIL, ONBOARDING_QUEUE, ONBOARDING_REJECTED, ONBOARDING_SUCCEED, ONBOARDING_UNQUALIFIED

TMP = "partner"
TMV = "volunteer"
DOCTORS_TYPS = [TMP, TMV]


class Doctor(Document):
    id = fields.UUIDField(primary_key=True)
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
    doctor_type = fields.StringField(choices=tuple(zip(range(len(DOCTORS_TYPS)), DOCTORS_TYPS)))
    duty_hours = fields.StringField(choices=tuple(zip(DEDICATE_HOURS_CHOICE, DEDICATE_HOURS_CHOICE)))
    onboarding_status = fields.StringField(choices=((ONBOARDING_SUCCEED, ONBOARDING_SUCCEED),
                                        (ONBOARDING_FAIL, ONBOARDING_FAIL),
                                        (ONBOARDING_REJECTED, ONBOARDING_REJECTED),
                                        (ONBOARDING_UNQUALIFIED, ONBOARDING_UNQUALIFIED),
                                        (ONBOARDING_QUEUE, ONBOARDING_QUEUE)))
    created_at = fields.DateTimeField(auto_now_add=True)
    freshdesk_agent_created = fields.BooleanField()
    comment = fields.StringField()
    meta_status = fields.StringField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        self.duty_hours = DEDICATE_HOURS_CHOICE[int(self.duty_hours)]
        return super(Doctor, self).save(*args, **kwargs)

   # def create(self, validated_data):
    #     if not self.id:
    #         validated_data[id] = uuid.UUID()
    #     return Doctor.objects.create(**validated_data)
    #
    # class Meta:
    #     ordering = ['created_at']
    #

