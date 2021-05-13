from django.utils.translation import ugettext_lazy as _
from djchoices import ChoiceItem, DjangoChoices


class GenderChoices(DjangoChoices):
    male = ChoiceItem(value="MALE", label=_("Male"))
    female = ChoiceItem(value="FEMALE", label=_("Female"))
    other = ChoiceItem(value="OTHER", label=_("Other"))

class BloodGroup(DjangoChoices):
    a_positive = ChoiceItem(value="A+", label=_("A+"))
    a_negative = ChoiceItem(value="A-", label=_("A-"))
    b_positive = ChoiceItem(value="B+", label=_("B+"))
    b_negative = ChoiceItem(value="B-", label=_("B-"))
    o_positive = ChoiceItem(value="O+", label=_("O+"))
    o_negative = ChoiceItem(value="O-", label=_("O-"))
    ab_positive = ChoiceItem(value="AB+", label=_("AB+"))
    ab_negative = ChoiceItem(value="AB-", label=_("AB-"))

class CovidUserType(DjangoChoices):
    donor = ChoiceItem(value="DONOR", label=_("Donor"))
    recipeint = ChoiceItem(value="RECIPEINT", label=_("Recipeint"))
