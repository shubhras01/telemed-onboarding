from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Staff(AbstractUser):
    STAFF_ONBOARDING_STATUS = (
        ('NOT_ONBOARDED', 'NOT_ONBOARDED'),
        ('ONBOARDED', 'ONBOARDED'),
    )

    onboarding_status = models.CharField(
        max_length=100,
        choices=STAFF_ONBOARDING_STATUS,
        default=STAFF_ONBOARDING_STATUS[0][0]
    )
    address = models.CharField(max_length=500, null=True, blank=True)
    pincode = models.IntegerField(default=560000)

    # todo-saran (Correct the format)
    availability_status = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name='Staff'