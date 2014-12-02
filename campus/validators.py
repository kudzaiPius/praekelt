from django.core.exceptions import ValidationError
import datetime

"""Validation method to ensure a given birthdate is atleast 18 years in the past."""
def validate_over_18(value):
	dt = datetime.date.today()

	yr = dt.year

	if value > dt.replace(year=yr-18):
		raise ValidationError("Invalid age : candidate must be atleast 18 years old.")

""""""
def validate_name(str):
	if str.isalpha() or str.isnumeric():
		raise ValidationError("Invalid entry : name cannot contain numbers.")