from user.models import User
from covid.constants import BloodGroup, CovidUserType
from django.db import models


class Referrer(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        app_label = 'covid'

    def __str__(self):
        return f'{self.id}: {self.name}'


class CovidUserDetail(models.Model):
    user = models.OneToOneField(
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

    class Meta:
        app_label = 'covid'

    def __str__(self):
        return f'{self.id}: {self.user.name}'
