from datetime import datetime
from django.forms import ModelForm, DateField, SelectDateWidget


from covid.models import CovidUserDetail
from user.models import User


class CovidUserForm(ModelForm):
    YEARS = [x for x in range(2019, 2023)]

    dob = DateField(
        widget=SelectDateWidget(
            years=YEARS,
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
        initial=datetime.now()
    )

    class Meta:
        model = User
        fields = (
            'name', 'gender',
            'dob',
            'address', 'city',
            'contact_number'
        )


class CovidUserDetailForm(ModelForm):
    YEARS = [x for x in range(2019, 2023)]

    covid_positive_date = DateField(
        widget=SelectDateWidget(
            years=YEARS,
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
        initial=datetime.now()
    )
    covid_negate_date = DateField(
        widget=SelectDateWidget(
            years=YEARS,
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
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
