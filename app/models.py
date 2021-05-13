from app.utils import mobile_validator
from app.constants import BloodGroup, CovidUserType, GenderChoices
from django.db import models
from app.dj_city import CITIES


class Referrer(models.Model):
    name = models.CharField(max_length=30)


class Locality(models.Model):
    city = models.CharField(choices=CITIES, null=False, max_length=20)


class User(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    dob = models.DateField()
    address = models.CharField(max_length=300, null=True, blank=True)
    locality = models.ForeignKey(Locality, db_index=True,
                                 related_name='app_locality',
                                 on_delete=models.DO_NOTHING,
                                 null=True, blank=True)
    contact_number = models.CharField(max_length=32, db_index=True,
                                      validators=[mobile_validator],
                                      unique=True)


class CovidUserDetail(models.Model):
    user = models.ForeignKey(
            User, db_index=True,
            related_name='app_user',
            on_delete=models.DO_NOTHING)
    user_type = models.CharField(max_length=20, choices=CovidUserType.choices)
    blood_group = models.CharField(max_length=20, choices=BloodGroup.choices)
    covid_positive_date = models.DateField()
    covid_negate_date = models.DateField(null=True, blank=True)
    point_of_contact = models.ForeignKey(Referrer, db_index=True,
                                         related_name='app_referrer',
                                         on_delete=models.DO_NOTHING,
                                         null=True, blank=True)
    recovered_contacts = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
