from django.core.exceptions import ValidationError
import os
def file_size(value): 
    filesize= value.size
    if filesize > 2097152:
        raise ValidationError("The maximum file size that can be uploaded is 2MB.")
    else:
        return value


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File provided should be a .pdf file.')