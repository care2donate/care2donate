from django.utils.translation import ugettext_lazy as _
from djchoices import ChoiceItem, DjangoChoices


class GenderChoices(DjangoChoices):
    male = ChoiceItem(value="MALE", label=_("Male"))
    female = ChoiceItem(value="FEMALE", label=_("Female"))
    other = ChoiceItem(value="OTHER", label=_("Other"))
