from datetime import datetime
from django.db import models
from user.constants import GenderChoices
from user.dj_city import CITIES
from user.utils import mobile_validator


class State(models.Model):
    name = models.CharField(max_length=30, db_index=True,
                            unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'user'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    state = models.ForeignKey(State, db_index=True,
                              related_name='city_state',
                              on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=30, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'user'
        unique_together = [('state', 'name')]

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    dob = models.DateField()
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.ForeignKey(City, db_index=True,
                             related_name='user_city',
                             on_delete=models.DO_NOTHING,
                             null=True, blank=True)
    contact_number = models.CharField(max_length=32, db_index=True,
                                      validators=[mobile_validator],
                                      unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'user'

    def __str__(self):
        return f'{self.id}: {self.name}'
