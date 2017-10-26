from django.core.exceptions import ValidationError


#Validation Function
def validate_content(value):
	content = value
	if content == "":
		raise ValidationError("Content cannot be blank")
	return value
