from django import forms
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.pptx', '.txt']
    #, '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls', '.mp4', '.mov']
    if not ext.lower() in valid_extensions:
        raise forms.ValidationError('Unsupported file extension.')
    
    filesize= value.size

    if filesize > 10485760:
        raise forms.ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value