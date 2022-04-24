import os


def upload_to(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    instance.attachment.open()
    filename_base, filename_ext = os.path.splitext(filename)

    return "{0}".format(instance.attachment)