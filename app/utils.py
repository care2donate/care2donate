import re
from django.core.exceptions import ValidationError


def mobile_validator(value):
    # regex for validating a generic international phone number
    regex = r'^(\+|00){0,2}(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$'
    rule = re.compile(regex)
    if not rule.search(value):
        msg = "Invalid mobile number."
        raise ValidationError(msg)