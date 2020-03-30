from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Staff(User):
    STAFF_ONBOARDING_STATUS = (
        (1, 'NOT_ONBOARDED'),
        (2, 'ONBOARDED'),
    )

    onboarding_status = models.IntegerField(choices=STAFF_ONBOARDING_STATUS, default=STAFF_ONBOARDING_STATUS[1])
    address = models.CharField(max_length=500, null=True, blank=True)
    pincode = models.IntegerField(default=560000)

    # todo-saran (Correct the format)
    availability_status = models.CharField(max_length=500, null=True, blank=True)
    meta = models.CharField(max_length=500, null=True, blank=True)
