from django.core.exceptions import ValidationError

def file_size(value):
    filesize = value.size
    if file_size>200000000:
        raise ValidationError("maximum size is 200 mb")