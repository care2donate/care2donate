from datetime import datetime
from django.forms import ModelForm, DateField, SelectDateWidget


from covid.models import CovidUserDetail
from user.models import User
from bootstrap_datepicker_plus import DatePickerInput


class CovidUserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'name', 'gender',
            'dob',
            'address', 'city',
            'contact_number'
        )
        widgets = {
            'dob': DatePickerInput(
                format='DD/MM/YYYY',
            ),
        }


class CovidUserDetailForm(ModelForm):
    YEARS = [x for x in range(2019, 2023)]

    covid_positive_date = DateField(
        widget=DatePickerInput(
            years=YEARS,
            format='DD/MM/YYYY',),
        initial=datetime.now()
    )
    covid_negate_date = DateField(
        widget=DatePickerInput(
            format='DD/MM/YYYY',
        ),
        initial=datetime.now()
    )

    class Meta:
        model = CovidUserDetail
        fields = (
            'user_type', 'blood_group',
            'covid_positive_date', 'covid_negate_date',
            'remarks',
        )
