from django import forms

from covid.models import CovidUserDetail
from user.models import User


class CovidUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'name', 'gender', 'dob',
            'address', 'city',
            'contact_number'
        )


class CovidUserDetailForm(forms.ModelForm):
    class Meta:
        model = CovidUserDetail
        fields = (
            'user_type', 'blood_group', 'covid_positive_date',
            'covid_negate_date', 'remarks',
        )
