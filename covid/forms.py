from datetime import datetime
from django import forms
from django.forms import ModelForm, DateField


from covid.models import CovidUserDetail
from user.models import City, State, User
from bootstrap_datepicker_plus import DatePickerInput


class LocalityForm(forms.Form):
    state_objs = State.objects.prefetch_related('city_state').order_by('name')
    first_state = state_objs.first()

    city_objs = City.objects.filter(state=first_state).order_by('name')
    first_city = city_objs.first()

    state = forms.ModelChoiceField(
        # empty_label='Not Specified',
        queryset=state_objs,
        # widget=forms.Select(attrs={"onChange": 'getCity(this.value)'}),
        initial=first_state
    )

    city = forms.ModelChoiceField(
        # empty_label='Not Specified',
        queryset=city_objs,
        initial=first_city
    )


class CovidUserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'name', 'gender',
            'dob',
            'address',
            'contact_number'
        )
        widgets = {
            'dob': DatePickerInput(
                format='DD/MM/YYYY',
            ),
        }


class CovidUserDetailForm(ModelForm):

    covid_positive_date = DateField(
        widget=DatePickerInput(
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
