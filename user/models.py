from datetime import datetime
from django.db import models
from user.constants import GenderChoices
from user.dj_city import CITIES
from user.utils import mobile_validator


class Locality(models.Model):
    city = models.CharField(choices=CITIES, null=False,
                            max_length=20, unique=True)

    created = models.DateTimeField(default=datetime.now())
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'user'

    def __str__(self):
        return f'{self.id}: {self.city}'


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

    created = models.DateTimeField(default=datetime.now())
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'user'

    def __str__(self):
        return f'{self.id}: {self.name}'
